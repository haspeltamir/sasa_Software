#!/usr/bin/env python3

"""
Simple startup script for SASA Software Microservices
Works on both Windows and Unix systems
"""

import os
import sys
import time
import subprocess
import threading
import signal
from pathlib import Path

class ServiceRunner:
    def __init__(self):
        self.logger_process = None
        self.watcher_process = None
        self.running = True
        
    def create_directories(self):
        """Create required directories"""
        directories = ['watched', 'processed', 'logs', 'temp']
        for dir_name in directories:
            Path(dir_name).mkdir(exist_ok=True)
            print(f"📁 Ensured directory exists: {dir_name}")
    
    def start_logger_service(self):
        """Start the logger service in a separate process"""
        try:
            print("🔧 Starting Logger Service...")
            self.logger_process = subprocess.Popen([
                sys.executable, "logger-service/logger.py"
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Wait a moment and check if it's still running
            time.sleep(2)
            if self.logger_process.poll() is None:
                print("✅ Logger Service started successfully")
                return True
            else:
                print("❌ Logger Service failed to start")
                return False
                
        except Exception as e:
            print(f"❌ Failed to start Logger Service: {e}")
            return False
    
    def start_watcher_service(self):
        """Start the watcher service"""
        try:
            print("👁️ Starting Watcher Service...")
            self.watcher_process = subprocess.Popen([
                sys.executable, "watcher-service/watcher.py"
            ])
            return True
        except Exception as e:
            print(f"❌ Failed to start Watcher Service: {e}")
            return False
    
    def signal_handler(self, signum, frame):
        """Handle shutdown signals"""
        print("\n🛑 Shutdown signal received. Stopping services...")
        self.stop_services()
        sys.exit(0)
    
    def stop_services(self):
        """Stop all services"""
        self.running = False
        
        if self.watcher_process:
            print("🛑 Stopping Watcher Service...")
            self.watcher_process.terminate()
            try:
                self.watcher_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.watcher_process.kill()
        
        if self.logger_process:
            print("🛑 Stopping Logger Service...")
            self.logger_process.terminate()
            try:
                self.logger_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.logger_process.kill()
    
    def run(self):
        """Main run method"""
        print("🚀 SASA Software Microservices Startup")
        print("=" * 40)
        
        # Setup signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, self.signal_handler)
        if hasattr(signal, 'SIGTERM'):
            signal.signal(signal.SIGTERM, self.signal_handler)
        
        # Create directories
        self.create_directories()
        
        # Start Logger Service
        if not self.start_logger_service():
            return False
        
        # Wait a moment for logger to initialize
        time.sleep(3)
        
        # Display information
        print("\n📊 Service Information:")
        print("   • Logger Service:      http://localhost:8001")
        print("   • Logger Config UI:    http://localhost:8081")
        print("   • Watcher Config UI:   http://localhost:8080")
        print("\n📁 Directories:")
        print("   • Watched:    ./watched")
        print("   • Processed:  ./processed")
        print("   • Logs:       ./logs")
        print("\n💡 To test the system, add a file to the './watched' directory.")
        print("🛑 Press Ctrl+C to stop all services.")
        print()
        
        # Start Watcher Service
        if not self.start_watcher_service():
            self.stop_services()
            return False
        
        # Wait for watcher service to complete
        try:
            if self.watcher_process:
                self.watcher_process.wait()
        except KeyboardInterrupt:
            pass
        
        # Cleanup
        self.stop_services()
        print("✅ All services stopped")
        return True


def main():
    """Main entry point"""
    # Check Python version
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required")
        sys.exit(1)
    
    # Check if we're in the right directory
    if not Path("logger-service").exists() or not Path("watcher-service").exists():
        print("❌ Please run this script from the SASA Software root directory")
        sys.exit(1)
    
    runner = ServiceRunner()
    try:
        success = runner.run()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        runner.stop_services()
        sys.exit(1)


if __name__ == "__main__":
    main()