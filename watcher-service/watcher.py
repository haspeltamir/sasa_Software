import os
import sys
import time
import shutil
import logging
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Add shared directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'shared'))

from utils import ConfigManager, NotificationHandler, setup_logging, get_file_hash, sanitize_filename
from jwt_manager import JWTManager


class FileProcessor:
    """Handles file processing and metadata extraction"""
    
    def __init__(self, config: dict, jwt_manager: JWTManager, notification_handler: NotificationHandler):
        self.config = config
        self.jwt_manager = jwt_manager
        self.notification_handler = notification_handler
        self.logger = logging.getLogger(__name__)
        
        # Ensure directories exist
        self._ensure_directories()
    
    def _ensure_directories(self):
        """Ensure all required directories exist"""
        directories = [
            self.config['directories']['watched'],
            self.config['directories']['processed'],
            self.config['directories'].get('temp', './temp')
        ]
        
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
    
    def extract_metadata(self, file_path: str) -> Dict[str, Any]:
        """Extract metadata from a file"""
        try:
            file_stat = os.stat(file_path)
            file_hash = get_file_hash(file_path)
            
            metadata = {
                "filename": os.path.basename(file_path),
                "created_at": datetime.utcnow().isoformat() + "Z",
                "file_size": file_stat.st_size,
                "hash": file_hash
            }
            
            self.logger.debug(f"Extracted metadata for {file_path}: {metadata}")
            return metadata
            
        except Exception as e:
            self.logger.error(f"Failed to extract metadata from {file_path}: {e}")
            raise
    
    def send_metadata_to_logger(self, metadata: Dict[str, Any]) -> bool:
        """Send metadata to logger service"""
        try:
            # Create JWT token
            token = self.jwt_manager.create_token(
                issuer=self.config['jwt']['issuer'],
                expiry_minutes=self.config['jwt']['expiry_minutes']
            )
            
            # Prepare request
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }
            
            url = f"{self.config['logger_service']['url']}{self.config['logger_service']['endpoint']}"
            timeout = self.config['logger_service']['timeout_seconds']
            
            # Send request
            response = requests.post(url, json=metadata, headers=headers, timeout=timeout)
            
            if response.status_code == 200:
                self.logger.info(f"Successfully sent metadata for {metadata['filename']}")
                return True
            else:
                self.logger.error(f"Logger service returned {response.status_code}: {response.text}")
                return False
                
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to send metadata to logger service: {e}")
            self.notification_handler.notify_error(f"Failed to send metadata for {metadata.get('filename', 'unknown')}", e)
            return False
        except Exception as e:
            self.logger.error(f"Unexpected error sending metadata: {e}")
            self.notification_handler.notify_error(f"Unexpected error processing {metadata.get('filename', 'unknown')}", e)
            return False
    
    def move_file_to_processed(self, source_path: str) -> bool:
        """Move file to processed directory"""
        try:
            filename = os.path.basename(source_path)
            processed_dir = self.config['directories']['processed']
            destination_path = os.path.join(processed_dir, filename)
            
            # Handle duplicate filenames
            counter = 1
            original_destination = destination_path
            while os.path.exists(destination_path):
                name, ext = os.path.splitext(original_destination)
                destination_path = f"{name}_{counter}{ext}"
                counter += 1
            
            shutil.move(source_path, destination_path)
            self.logger.info(f"Moved {filename} to processed directory: {destination_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to move file {source_path}: {e}")
            self.notification_handler.notify_error(f"Failed to move file {source_path}", e)
            return False
    
    def process_file(self, file_path: str) -> bool:
        """Process a single file"""
        self.logger.info(f"Processing file: {file_path}")
        
        try:
            # Check file size limit
            file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
            max_size_mb = self.config['processing']['file_size_limit_mb']
            
            if file_size_mb > max_size_mb:
                self.logger.warning(f"File {file_path} exceeds size limit ({file_size_mb:.2f}MB > {max_size_mb}MB)")
                return False
            
            # Check file extension
            supported_extensions = self.config['processing']['supported_extensions']
            if supported_extensions:
                file_ext = Path(file_path).suffix.lower()
                if file_ext not in supported_extensions:
                    self.logger.warning(f"File {file_path} has unsupported extension: {file_ext}")
                    return False
            
            # Extract metadata
            metadata = self.extract_metadata(file_path)
            
            # Send to logger service with retry logic
            max_attempts = self.config['logger_service']['retry_attempts']
            retry_delay = self.config['logger_service']['retry_delay_seconds']
            
            for attempt in range(max_attempts):
                if self.send_metadata_to_logger(metadata):
                    # Success - move file to processed
                    if self.config['monitoring']['move_processed_files']:
                        return self.move_file_to_processed(file_path)
                    return True
                
                if attempt < max_attempts - 1:
                    self.logger.warning(f"Retry {attempt + 1}/{max_attempts} for {file_path} in {retry_delay}s")
                    time.sleep(retry_delay)
            
            self.logger.error(f"Failed to process {file_path} after {max_attempts} attempts")
            return False
            
        except Exception as e:
            self.logger.error(f"Error processing file {file_path}: {e}")
            self.notification_handler.notify_error(f"Error processing file {file_path}", e)
            return False


class WatcherEventHandler(FileSystemEventHandler):
    """Handles file system events for directory monitoring"""
    
    def __init__(self, file_processor: FileProcessor, config: dict):
        super().__init__()
        self.file_processor = file_processor
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.pending_files = set()
    
    def _should_process_file(self, file_path: str) -> bool:
        """Check if file should be processed based on configuration"""
        # Check exclude patterns
        filename = os.path.basename(file_path)
        exclude_patterns = self.config['processing']['exclude_patterns']
        
        import fnmatch
        for pattern in exclude_patterns:
            if fnmatch.fnmatch(filename, pattern):
                return False
        
        # Check if file is complete (not being written)
        try:
            # Simple check - try to rename file to itself
            os.rename(file_path, file_path)
            return True
        except OSError:
            # File is likely being written to
            return False
    
    def on_created(self, event):
        """Handle file creation events"""
        if event.is_directory:
            return
        
        file_path = event.src_path
        self.logger.debug(f"File created: {file_path}")
        
        if self._should_process_file(file_path):
            self.pending_files.add(file_path)
            self.logger.info(f"Added {file_path} to processing queue")
    
    def process_pending_files(self):
        """Process all pending files"""
        if not self.pending_files:
            return
        
        files_to_process = list(self.pending_files)[:self.config['processing']['max_files_to_process']]
        
        for file_path in files_to_process:
            if os.path.exists(file_path) and self._should_process_file(file_path):
                success = self.file_processor.process_file(file_path)
                if success:
                    self.pending_files.discard(file_path)
            else:
                # File no longer exists or is not ready
                self.pending_files.discard(file_path)


class WatcherService:
    """Main watcher service class"""
    
    def __init__(self, config_path: str):
        self.config = ConfigManager.load_config(config_path)
        
        # Setup logging
        setup_logging(
            self.config['service_name'],
            self.config['logging']['level'],
            self.config['logging']['file']
        )
        
        self.logger = logging.getLogger(__name__)
        self.logger.info("Initializing Watcher Service")
        
        # Initialize components
        self.notification_handler = NotificationHandler(self.config)
        self.jwt_manager = JWTManager(self.config['jwt']['secret'])
        self.file_processor = FileProcessor(self.config, self.jwt_manager, self.notification_handler)
        
        # Setup file system monitoring
        self.observer = Observer()
        self.event_handler = WatcherEventHandler(self.file_processor, self.config)
        
        self.running = False
    
    def start(self):
        """Start the watcher service"""
        try:
            watched_dir = os.path.abspath(self.config['directories']['watched'])
            self.logger.info(f"Starting to watch directory: {watched_dir}")
            
            # Start file system observer
            self.observer.schedule(self.event_handler, watched_dir, recursive=False)
            self.observer.start()
            
            self.running = True
            self.logger.info("Watcher Service started successfully")
            
            # Main loop
            poll_interval = self.config['monitoring']['poll_interval_seconds']
            
            while self.running:
                try:
                    # Process pending files
                    if self.config['monitoring']['batch_processing']:
                        self.event_handler.process_pending_files()
                    
                    time.sleep(poll_interval)
                    
                except KeyboardInterrupt:
                    self.logger.info("Received shutdown signal")
                    break
                except Exception as e:
                    self.logger.error(f"Error in main loop: {e}")
                    self.notification_handler.notify_error("Error in watcher main loop", e)
                    time.sleep(poll_interval)
        
        except Exception as e:
            self.logger.error(f"Failed to start watcher service: {e}")
            self.notification_handler.notify_error("Failed to start watcher service", e)
            raise
        
        finally:
            self.stop()
    
    def stop(self):
        """Stop the watcher service"""
        self.logger.info("Stopping Watcher Service")
        self.running = False
        
        if self.observer.is_alive():
            self.observer.stop()
            self.observer.join()
        
        self.logger.info("Watcher Service stopped")


def main():
    """Main entry point"""
    try:
        config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
        service = WatcherService(config_path)
        service.start()
        
    except KeyboardInterrupt:
        print("\nShutdown requested by user")
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()