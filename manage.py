#!/usr/bin/env python3

"""
SASA Software Management Script
Provides easy management commands for the microservices system
"""

import argparse
import os
import sys
import subprocess
import time
import requests
from pathlib import Path

class SASAManager:
    """Management class for SASA Software services"""
    
    def __init__(self):
        self.services = {
            'logger': 'http://localhost:8001',
            'watcher-config': 'http://localhost:8080', 
            'logger-config': 'http://localhost:8081'
        }
    
    def check_docker(self):
        """Check if Docker is available"""
        try:
            subprocess.run(['docker', '--version'], capture_output=True, check=True)
            subprocess.run(['docker-compose', '--version'], capture_output=True, check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    def start_services(self):
        """Start all services using Docker Compose"""
        print("🚀 Starting SASA Software services...")
        
        if not self.check_docker():
            print("❌ Docker or Docker Compose not found. Please install Docker first.")
            return False
        
        # Create directories
        dirs = ['watched', 'processed', 'logs', 'temp']
        for dir_name in dirs:
            Path(dir_name).mkdir(exist_ok=True)
            print(f"📁 Created directory: {dir_name}")
        
        # Start services
        try:
            subprocess.run(['docker-compose', 'up', '--build', '-d'], check=True)
            print("⏳ Waiting for services to start...")
            time.sleep(10)
            
            # Check service health
            self.check_status()
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to start services: {e}")
            return False
    
    def stop_services(self):
        """Stop all services"""
        print("🛑 Stopping SASA Software services...")
        try:
            subprocess.run(['docker-compose', 'down'], check=True)
            print("✅ Services stopped successfully")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to stop services: {e}")
            return False
    
    def restart_services(self):
        """Restart all services"""
        print("🔄 Restarting SASA Software services...")
        self.stop_services()
        time.sleep(2)
        return self.start_services()
    
    def check_status(self):
        """Check status of all services"""
        print("🔍 Checking service status...")
        
        # Check Logger Service
        try:
            response = requests.get(f"{self.services['logger']}/health", timeout=5)
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Logger Service: {data.get('status', 'unknown')}")
                print(f"   Processed files: {data.get('processed_files_count', 0)}")
                print(f"   Uptime: {data.get('uptime_seconds', 0)}s")
            else:
                print(f"⚠️ Logger Service: HTTP {response.status_code}")
        except requests.exceptions.RequestException:
            print("❌ Logger Service: Not responding")
        
        # Check Configuration UIs
        for name, url in [('Watcher Config UI', self.services['watcher-config']), 
                         ('Logger Config UI', self.services['logger-config'])]:
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    print(f"✅ {name}: Running")
                else:
                    print(f"⚠️ {name}: HTTP {response.status_code}")
            except requests.exceptions.RequestException:
                print(f"❌ {name}: Not responding")
    
    def show_logs(self, service=None, follow=False):
        """Show service logs"""
        cmd = ['docker-compose', 'logs']
        if follow:
            cmd.append('-f')
        if service:
            cmd.append(service)
        
        try:
            subprocess.run(cmd)
        except KeyboardInterrupt:
            print("\n📋 Log viewing stopped")
    
    def show_stats(self):
        """Show system statistics"""
        print("📊 SASA Software Statistics")
        print("=" * 40)
        
        # Count files in directories
        dirs = {
            'Watched': 'watched',
            'Processed': 'processed', 
            'Logs': 'logs'
        }
        
        for name, path in dirs.items():
            dir_path = Path(path)
            if dir_path.exists():
                files = list(dir_path.glob('*'))
                files = [f for f in files if f.is_file()]
                print(f"{name:12}: {len(files)} files")
            else:
                print(f"{name:12}: Directory not found")
        
        # Service status
        print("\n🔧 Service Status:")
        for name, url in self.services.items():
            try:
                response = requests.get(url if 'health' in url else f"{url}/health" if name == 'logger' else url, timeout=2)
                status = "✅ Running" if response.status_code == 200 else f"⚠️ HTTP {response.status_code}"
            except:
                status = "❌ Down"
            print(f"{name:15}: {status}")
    
    def cleanup(self):
        """Clean up system (remove processed files and logs)"""
        print("🧹 Cleaning up SASA Software...")
        
        confirm = input("This will delete processed files and logs. Continue? (y/N): ")
        if confirm.lower() != 'y':
            print("Cleanup cancelled")
            return
        
        # Clean directories
        dirs_to_clean = ['processed', 'logs']
        for dir_name in dirs_to_clean:
            dir_path = Path(dir_name)
            if dir_path.exists():
                files = list(dir_path.glob('*'))
                for file_path in files:
                    if file_path.is_file():
                        file_path.unlink()
                print(f"🗑️ Cleaned {len(files)} files from {dir_name}")
        
        print("✅ Cleanup completed")
    
    def test_system(self):
        """Run system tests"""
        print("🧪 Running system tests...")
        try:
            subprocess.run([sys.executable, 'test_system.py'], check=True)
        except subprocess.CalledProcessError:
            print("❌ Tests failed")
        except FileNotFoundError:
            print("❌ test_system.py not found")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='SASA Software Management Tool')
    parser.add_argument('command', choices=[
        'start', 'stop', 'restart', 'status', 'logs', 'stats', 'cleanup', 'test'
    ], help='Command to execute')
    
    parser.add_argument('--service', help='Specific service for logs command')
    parser.add_argument('--follow', '-f', action='store_true', help='Follow logs')
    
    args = parser.parse_args()
    
    manager = SASAManager()
    
    if args.command == 'start':
        manager.start_services()
    elif args.command == 'stop':
        manager.stop_services()
    elif args.command == 'restart':
        manager.restart_services()
    elif args.command == 'status':
        manager.check_status()
    elif args.command == 'logs':
        manager.show_logs(args.service, args.follow)
    elif args.command == 'stats':
        manager.show_stats()
    elif args.command == 'cleanup':
        manager.cleanup()
    elif args.command == 'test':
        manager.test_system()

if __name__ == "__main__":
    main()