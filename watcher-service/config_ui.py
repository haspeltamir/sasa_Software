import os
import sys
import yaml
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

# Add shared directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'shared'))

from utils import ConfigManager, setup_logging

app = FastAPI(title="Watcher Service Configuration UI")
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))

config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
current_config = {}

def load_current_config():
    """Load current configuration"""
    global current_config
    try:
        current_config = ConfigManager.load_config(config_path)
    except Exception as e:
        current_config = {}
        print(f"Failed to load config: {e}")

def save_config(config_data: dict):
    """Save configuration to file"""
    try:
        with open(config_path, 'w', encoding='utf-8') as file:
            yaml.dump(config_data, file, default_flow_style=False)
        return True
    except Exception as e:
        print(f"Failed to save config: {e}")
        return False

@app.on_event("startup")
async def startup_event():
    load_current_config()

@app.get("/", response_class=HTMLResponse)
async def get_config_form(request: Request):
    """Display configuration form"""
    return templates.TemplateResponse("config_form.html", {
        "request": request,
        "config": current_config
    })

@app.post("/save")
async def save_configuration(
    request: Request,
    service_name: str = Form(...),
    jwt_secret: str = Form(...),
    issuer: str = Form(...),
    watch_directory: str = Form(...),
    processed_directory: str = Form(...),
    temp_directory: str = Form(...),
    enable_nested_monitoring: bool = Form(False),
    file_patterns: str = Form(...),
    excluded_patterns: str = Form(""),
    include_hidden_files: bool = Form(False),
    watch_timeout: int = Form(...),
    processing_delay: int = Form(...),
    retry_attempts: int = Form(...),
    retry_delay: int = Form(...),
    logger_service_url: str = Form(...),
    logger_endpoint: str = Form(...),
    connection_timeout: int = Form(...),
    request_timeout: int = Form(...),
    log_level: str = Form(...),
    log_file: str = Form(...),
    max_size_mb: int = Form(...),
    backup_count: int = Form(...),
    email_enabled: bool = Form(False),
    smtp_server: str = Form(""),
    smtp_port: int = Form(587),
    smtp_user: str = Form(""),
    use_tls: bool = Form(False),
    recipients: str = Form(""),
    syslog_enabled: bool = Form(False),
    syslog_facility: str = Form("LOG_USER"),
    checksum_algorithm: str = Form(...),
    enable_content_preview: bool = Form(False),
    content_preview_size: int = Form(256),
    enable_file_validation: bool = Form(False),
    max_file_size_mb: int = Form(...),
    min_file_age_seconds: int = Form(...)
):
    """Save configuration"""
    try:
        # Parse file patterns
        patterns = []
        if file_patterns.strip():
            patterns = [pattern.strip() for pattern in file_patterns.split(',') if pattern.strip()]
        else:
            patterns = ["*"]
        
        # Parse excluded patterns
        excluded = []
        if excluded_patterns.strip():
            excluded = [pattern.strip() for pattern in excluded_patterns.split(',') if pattern.strip()]
        
        # Parse email recipients
        email_recipients = []
        if recipients.strip():
            email_recipients = [email.strip() for email in recipients.split(',') if email.strip()]
        
        # Build configuration dictionary
        config_data = {
            "service_name": service_name,
            "jwt": {
                "secret": jwt_secret,
                "issuer": issuer,
                "algorithm": "HS256"
            },
            "directories": {
                "watch_directory": watch_directory,
                "processed_directory": processed_directory,
                "temp_directory": temp_directory
            },
            "monitoring": {
                "enable_nested_monitoring": enable_nested_monitoring,
                "file_patterns": patterns,
                "excluded_patterns": excluded,
                "include_hidden_files": include_hidden_files,
                "watch_timeout": watch_timeout
            },
            "processing": {
                "processing_delay": processing_delay,
                "retry_attempts": retry_attempts,
                "retry_delay": retry_delay
            },
            "communication": {
                "logger_service_url": logger_service_url,
                "logger_endpoint": logger_endpoint,
                "connection_timeout": connection_timeout,
                "request_timeout": request_timeout
            },
            "logging": {
                "level": log_level,
                "file": log_file,
                "max_size_mb": max_size_mb,
                "backup_count": backup_count,
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            },
            "notifications": {
                "email": {
                    "enabled": email_enabled,
                    "smtp_server": smtp_server,
                    "smtp_port": smtp_port,
                    "smtp_user": smtp_user,
                    "smtp_password": "",
                    "use_tls": use_tls,
                    "recipients": email_recipients
                },
                "syslog": {
                    "enabled": syslog_enabled,
                    "facility": syslog_facility
                }
            },
            "file_analysis": {
                "checksum_algorithm": checksum_algorithm,
                "enable_content_preview": enable_content_preview,
                "content_preview_size": content_preview_size
            },
            "validation": {
                "enable_file_validation": enable_file_validation,
                "max_file_size_mb": max_file_size_mb,
                "min_file_age_seconds": min_file_age_seconds
            }
        }
        
        if save_config(config_data):
            load_current_config()
            return templates.TemplateResponse("config_form.html", {
                "request": request,
                "config": current_config,
                "success_message": "Configuration saved successfully!"
            })
        else:
            raise HTTPException(status_code=500, detail="Failed to save configuration")
            
    except Exception as e:
        return templates.TemplateResponse("config_form.html", {
            "request": request,
            "config": current_config,
            "error_message": f"Error saving configuration: {e}"
        })

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "watcher-config-ui"}

def main():
    """Run the configuration UI"""
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8082,
        log_level="info"
    )

if __name__ == "__main__":
    main()