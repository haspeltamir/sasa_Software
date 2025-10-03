import os
import logging
import smtplib
try:
    import syslog
    HAS_SYSLOG = True
except ImportError:
    # syslog is not available on Windows
    HAS_SYSLOG = False
    syslog = None
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional, List
from datetime import datetime
import yaml


class NotificationHandler:
    """Handles various notification methods for errors and alerts"""
    
    def __init__(self, config: dict):
        self.config = config
        self.email_config = config.get('notifications', {}).get('email', {})
        self.syslog_config = config.get('notifications', {}).get('syslog', {})
        
    def send_email(self, subject: str, message: str, recipients: List[str] = None):
        """Send email notification"""
        if not self.email_config.get('enabled', False):
            return
            
        try:
            recipients = recipients or self.email_config.get('recipients', [])
            if not recipients:
                return
                
            msg = MIMEMultipart()
            msg['From'] = self.email_config['smtp_user']
            msg['To'] = ', '.join(recipients)
            msg['Subject'] = f"[SASA-Software] {subject}"
            
            body = f"""
            Time: {datetime.utcnow().isoformat()}Z
            Service: {self.config.get('service_name', 'Unknown')}
            
            {message}
            """
            
            msg.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port']) as server:
                if self.email_config.get('use_tls', True):
                    server.starttls()
                server.login(self.email_config['smtp_user'], self.email_config['smtp_password'])
                server.sendmail(self.email_config['smtp_user'], recipients, msg.as_string())
                
            logging.info(f"Email notification sent: {subject}")
            
        except Exception as e:
            logging.error(f"Failed to send email notification: {e}")
    
    def send_syslog(self, level: str, message: str):
        """Send syslog notification"""
        if not self.syslog_config.get('enabled', False):
            return
        
        if not HAS_SYSLOG:
            logging.warning("Syslog is not available on this platform (Windows). Using Windows Event Log instead.")
            self._send_windows_event_log(level, message)
            return
            
        try:
            # Map string levels to syslog levels
            level_map = {
                'debug': syslog.LOG_DEBUG,
                'info': syslog.LOG_INFO,
                'warning': syslog.LOG_WARNING,
                'error': syslog.LOG_ERR,
                'critical': syslog.LOG_CRIT
            }
            
            syslog_level = level_map.get(level.lower(), syslog.LOG_INFO)
            facility = getattr(syslog, self.syslog_config.get('facility', 'LOG_USER'))
            
            syslog.openlog(
                ident=self.config.get('service_name', 'sasa-software'),
                logoption=syslog.LOG_PID,
                facility=facility
            )
            
            syslog.syslog(syslog_level, message)
            syslog.closelog()
            
            logging.info(f"Syslog notification sent: {level} - {message}")
            
        except Exception as e:
            logging.error(f"Failed to send syslog notification: {e}")
    
    def _send_windows_event_log(self, level: str, message: str):
        """Send notification to Windows Event Log as fallback"""
        try:
            import subprocess
            
            # Use PowerShell to write to Windows Event Log
            ps_command = f'''
            if (-not (Get-EventLog -LogName Application -Source "SASA-Software" -ErrorAction SilentlyContinue)) {{
                New-EventLog -LogName Application -Source "SASA-Software"
            }}
            Write-EventLog -LogName Application -Source "SASA-Software" -EventId 1001 -EntryType Information -Message "{message}"
            '''
            
            subprocess.run(["powershell", "-Command", ps_command], 
                         capture_output=True, check=False)
            
            logging.info(f"Windows Event Log notification sent: {level} - {message}")
            
        except Exception as e:
            logging.error(f"Failed to send Windows Event Log notification: {e}")
    
    def notify_error(self, error_message: str, exception: Exception = None):
        """Send error notifications via all configured methods"""
        full_message = error_message
        if exception:
            full_message += f"\nException: {str(exception)}"
            
        # Send email notification
        self.send_email("System Error", full_message)
        
        # Send syslog notification
        self.send_syslog("error", full_message)


class ConfigManager:
    """Manages configuration loading and validation"""
    
    @staticmethod
    def load_config(config_path: str) -> dict:
        """Load configuration from YAML file"""
        try:
            with open(config_path, 'r', encoding='utf-8') as file:
                config = yaml.safe_load(file)
            
            # Load environment variables
            config = ConfigManager._load_env_variables(config)
            
            return config
        except Exception as e:
            raise Exception(f"Failed to load configuration: {e}")
    
    @staticmethod
    def _load_env_variables(config: dict) -> dict:
        """Load environment variables and override config values"""
        # JWT Secret
        jwt_secret = os.getenv('JWT_SECRET')
        if jwt_secret:
            config['jwt']['secret'] = jwt_secret
        
        # Email configuration
        if 'notifications' in config and 'email' in config['notifications']:
            email_config = config['notifications']['email']
            email_config['smtp_password'] = os.getenv('SMTP_PASSWORD', email_config.get('smtp_password', ''))
            email_config['smtp_user'] = os.getenv('SMTP_USER', email_config.get('smtp_user', ''))
        
        return config


def setup_logging(service_name: str, log_level: str = "INFO", log_file: str = None):
    """Setup logging configuration for the service"""
    
    # Create logs directory if it doesn't exist
    if log_file:
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    # Configure logging
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    # Create console handler with UTF-8 encoding for Windows
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter(log_format)
    console_handler.setFormatter(console_formatter)
    
    # Try to set UTF-8 encoding for console on Windows to handle Unicode paths
    if hasattr(console_handler.stream, 'reconfigure'):
        try:
            console_handler.stream.reconfigure(encoding='utf-8', errors='replace')
        except:
            pass
    
    handlers = [console_handler]
    
    if log_file:
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_formatter = logging.Formatter(log_format)
        file_handler.setFormatter(file_formatter)
        handlers.append(file_handler)
    
    # Clear any existing handlers and configure new ones
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format=log_format,
        handlers=handlers,
        force=True  # Force reconfiguration
    )
    
    # Set service name in logger
    logger = logging.getLogger(service_name)
    return logger


def sanitize_filename(filename: str) -> str:
    """Sanitize filename by replacing unsafe characters with underscores"""
    import re
    # Replace any character that is not alphanumeric, dot, hyphen, or underscore
    sanitized = re.sub(r'[^\w\-_\.]', '_', filename)
    return sanitized


def get_file_hash(file_path: str) -> str:
    """Calculate SHA256 hash of a file"""
    import hashlib
    
    hash_sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
    except Exception as e:
        logging.error(f"Failed to calculate hash for {file_path}: {e}")
        return ""