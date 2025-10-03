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

app = FastAPI(title="Logger Service Configuration UI")
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
    expected_issuer: str = Form(...),
    host: str = Form(...),
    port: int = Form(...),
    workers: int = Form(...),
    logs_directory: str = Form(...),
    file_retention_days: int = Form(...),
    max_log_files: int = Form(...),
    compress_old_logs: bool = Form(False),
    sanitize_filenames: bool = Form(False),
    timestamp_format: str = Form(...),
    content_template: str = Form(...),
    max_filename_length: int = Form(...),
    max_file_size_mb: int = Form(...),
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
    health_check_enabled: bool = Form(False),
    detailed_info: bool = Form(False),
    rate_limiting_enabled: bool = Form(False),
    requests_per_minute: int = Form(100),
    burst_size: int = Form(10),
    cors_enabled: bool = Form(False),
    allowed_origins: str = Form(""),
    request_size_limit_mb: int = Form(10)
):
    """Save configuration"""
    try:
        # Parse allowed origins
        origins = []
        if allowed_origins.strip():
            origins = [origin.strip() for origin in allowed_origins.split(',') if origin.strip()]
        else:
            origins = ["*"]
        
        # Parse email recipients
        email_recipients = []
        if recipients.strip():
            email_recipients = [email.strip() for email in recipients.split(',') if email.strip()]
        
        # Build configuration dictionary
        config_data = {
            "service_name": service_name,
            "jwt": {
                "secret": jwt_secret,
                "expected_issuer": expected_issuer,
                "algorithm": "HS256"
            },
            "server": {
                "host": host,
                "port": port,
                "workers": workers
            },
            "storage": {
                "logs_directory": logs_directory,
                "file_retention_days": file_retention_days,
                "max_log_files": max_log_files,
                "compress_old_logs": compress_old_logs
            },
            "processing": {
                "sanitize_filenames": sanitize_filenames,
                "timestamp_format": timestamp_format,
                "content_template": content_template
            },
            "validation": {
                "max_filename_length": max_filename_length,
                "max_file_size_mb": max_file_size_mb,
                "required_fields": ["filename", "created_at", "file_size"],
                "optional_fields": ["hash"]
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
            "health_check": {
                "enabled": health_check_enabled,
                "endpoint": "/health",
                "detailed_info": detailed_info
            },
            "rate_limiting": {
                "enabled": rate_limiting_enabled,
                "requests_per_minute": requests_per_minute,
                "burst_size": burst_size
            },
            "security": {
                "cors_enabled": cors_enabled,
                "allowed_origins": origins,
                "request_size_limit_mb": request_size_limit_mb
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
    return {"status": "healthy", "service": "logger-config-ui"}

def main():
    """Run the configuration UI"""
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8081,
        log_level="info"
    )

if __name__ == "__main__":
    main()