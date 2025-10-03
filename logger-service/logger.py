import os
import sys
import logging
import datetime
from pathlib import Path
from typing import Dict, Any, Optional
import re

from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, validator
import uvicorn

# Add shared directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'shared'))

from utils import ConfigManager, NotificationHandler, setup_logging, sanitize_filename
from jwt_manager import JWTManager


# Request Models
class LogRequest(BaseModel):
    filename: str
    created_at: str
    file_size: int
    hash: Optional[str] = None
    
    @validator('filename')
    def validate_filename(cls, v):
        if not v or len(v.strip()) == 0:
            raise ValueError('Filename cannot be empty')
        if len(v) > 255:
            raise ValueError('Filename too long (max 255 characters)')
        return v.strip()
    
    @validator('file_size')
    def validate_file_size(cls, v):
        if v < 0:
            raise ValueError('File size cannot be negative')
        return v
    
    @validator('created_at')
    def validate_created_at(cls, v):
        try:
            # Try to parse ISO 8601 format
            datetime.datetime.fromisoformat(v.replace('Z', '+00:00'))
            return v
        except ValueError:
            raise ValueError('Invalid datetime format, expected ISO 8601')


# Response Models
class LogResponse(BaseModel):
    message: str
    log_file: str
    processed_at: str


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str
    uptime_seconds: int
    processed_files_count: int
    last_processed: Optional[str] = None


class LoggerService:
    """Main logger service class"""
    
    def __init__(self, config: dict):
        self.config = config
        
        # Setup logging
        setup_logging(
            self.config['service_name'],
            self.config['logging']['level'],
            self.config['logging']['file']
        )
        
        self.logger = logging.getLogger(__name__)
        self.logger.info("Initializing Logger Service")
        
        # Initialize components
        self.notification_handler = NotificationHandler(self.config)
        self.jwt_manager = JWTManager(self.config['jwt']['secret'])
        
        # Ensure logs directory exists
        self.logs_dir = Path(self.config['storage']['logs_directory'])
        self.logs_dir.mkdir(parents=True, exist_ok=True)
        
        # Statistics
        self.start_time = datetime.datetime.utcnow()
        self.processed_files_count = 0
        self.last_processed = None
        
        # Setup FastAPI app
        self.app = FastAPI(
            title="Logger Service",
            description="Microservice for logging file metadata",
            version="1.0.0"
        )
        
        self._setup_routes()
        
        self.logger.info("Logger Service initialized successfully")
    
    def _setup_routes(self):
        """Setup FastAPI routes"""
        security = HTTPBearer()
        
        @self.app.middleware("http")
        async def log_requests(request: Request, call_next):
            start_time = datetime.datetime.utcnow()
            
            # Log incoming request
            self.logger.info(f"Incoming request: {request.method} {request.url.path}")
            
            response = await call_next(request)
            
            # Log response
            process_time = (datetime.datetime.utcnow() - start_time).total_seconds()
            self.logger.info(f"Request completed: {response.status_code} in {process_time:.3f}s")
            
            return response
        
        @self.app.post("/log", response_model=LogResponse)
        async def log_metadata(
            request: LogRequest,
            credentials: HTTPAuthorizationCredentials = Depends(security)
        ):
            """Log file metadata endpoint"""
            try:
                # Validate JWT token
                token = credentials.credentials
                payload = self.jwt_manager.validate_token(
                    token, 
                    self.config['jwt']['expected_issuer']
                )
                
                self.logger.info(f"Processing log request for file: {request.filename}")
                
                # Create log entry
                log_file_path = self._create_log_file(request)
                
                # Update statistics
                self.processed_files_count += 1
                self.last_processed = datetime.datetime.utcnow().isoformat() + "Z"
                
                self.logger.info(f"Successfully created log file: {log_file_path}")
                
                return LogResponse(
                    message="Log entry created successfully",
                    log_file=str(log_file_path),
                    processed_at=self.last_processed
                )
                
            except Exception as e:
                if "Invalid token" in str(e) or "expired" in str(e).lower():
                    self.logger.warning(f"Authentication failed: {e}")
                    raise HTTPException(status_code=401, detail="Invalid or expired token")
                elif "validation" in str(e).lower():
                    self.logger.warning(f"Validation error: {e}")
                    raise HTTPException(status_code=400, detail=f"Validation error: {e}")
                else:
                    self.logger.error(f"Internal error processing log request: {e}")
                    self.notification_handler.notify_error(f"Failed to process log request for {request.filename}", e)
                    raise HTTPException(status_code=500, detail="Internal server error")
        
        @self.app.get("/health", response_model=HealthResponse)
        async def health_check():
            """Health check endpoint"""
            uptime = (datetime.datetime.utcnow() - self.start_time).total_seconds()
            
            response = HealthResponse(
                status="healthy",
                service=self.config['service_name'],
                version="1.0.0",
                uptime_seconds=int(uptime),
                processed_files_count=self.processed_files_count,
                last_processed=self.last_processed
            )
            
            if self.config['health_check']['detailed_info']:
                self.logger.debug(f"Health check requested - Status: {response.status}")
            
            return response
        
        @self.app.get("/")
        async def root():
            """Root endpoint"""
            return {
                "service": self.config['service_name'],
                "status": "running",
                "endpoints": {
                    "log": "/log",
                    "health": "/health"
                }
            }
    
    def _create_log_file(self, request: LogRequest) -> Path:
        """Create log file with metadata"""
        try:
            # Sanitize filename
            original_filename = request.filename
            if self.config['processing']['sanitize_filenames']:
                base_filename = sanitize_filename(Path(original_filename).stem)
            else:
                base_filename = Path(original_filename).stem
            
            # Generate timestamp
            timestamp = datetime.datetime.utcnow().strftime(
                self.config['processing']['timestamp_format']
            )
            
            # Create log filename
            log_filename = f"{base_filename}-{timestamp}.txt"
            log_file_path = self.logs_dir / log_filename
            
            # Handle duplicate filenames
            counter = 1
            original_log_path = log_file_path
            while log_file_path.exists():
                stem = original_log_path.stem
                suffix = original_log_path.suffix
                log_file_path = self.logs_dir / f"{stem}_{counter}{suffix}"
                counter += 1
            
            # Format file size
            file_size_formatted = self._format_file_size(request.file_size)
            
            # Create log content
            processed_at = datetime.datetime.utcnow().isoformat() + "Z"
            
            content = self.config['processing']['content_template'].format(
                filename=original_filename,
                file_size_formatted=file_size_formatted,
                created_at=request.created_at,
                hash=request.hash or "N/A",
                processed_at=processed_at
            )
            
            # Write log file
            with open(log_file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            self.logger.debug(f"Created log file: {log_file_path}")
            return log_file_path
            
        except Exception as e:
            self.logger.error(f"Failed to create log file for {request.filename}: {e}")
            raise
    
    def _format_file_size(self, size_bytes: int) -> str:
        """Format file size in human-readable format"""
        if size_bytes < 1024:
            return f"{size_bytes}B"
        elif size_bytes < 1024 * 1024:
            return f"{size_bytes / 1024:.1f}KB"
        elif size_bytes < 1024 * 1024 * 1024:
            return f"{size_bytes / (1024 * 1024):.1f}MB"
        else:
            return f"{size_bytes / (1024 * 1024 * 1024):.1f}GB"
    
    def run(self):
        """Run the logger service"""
        try:
            self.logger.info(
                f"Starting Logger Service on {self.config['server']['host']}:{self.config['server']['port']}"
            )
            
            uvicorn.run(
                self.app,
                host=self.config['server']['host'],
                port=self.config['server']['port'],
                workers=self.config['server']['workers'],
                log_level=self.config['logging']['level'].lower()
            )
            
        except Exception as e:
            self.logger.error(f"Failed to start Logger Service: {e}")
            self.notification_handler.notify_error("Failed to start Logger Service", e)
            raise


def main():
    """Main entry point"""
    try:
        config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
        config = ConfigManager.load_config(config_path)
        
        service = LoggerService(config)
        service.run()
        
    except KeyboardInterrupt:
        print("\nShutdown requested by user")
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()