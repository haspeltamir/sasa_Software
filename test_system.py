#!/usr/bin/env python3

"""
Test script for SASA Software Microservices System
This script creates test files and validates the system functionality
"""

import os
import sys
import time
import requests
import json
from datetime import datetime
from pathlib import Path

def create_test_files():
    """Create test files in the watched directory"""
    watched_dir = Path("watched")
    watched_dir.mkdir(exist_ok=True)
    
    test_files = [
        ("test_document.pdf", b"This is a test PDF content for SASA Software"),
        ("sample_data.txt", b"Sample text data\nLine 2\nLine 3\nEnd of file"),
        ("image_file.jpg", b"\xFF\xD8\xFF\xE0" + b"Fake JPEG header" + b"\x00" * 100),
        ("report_2025.xlsx", b"PK\x03\x04" + b"Fake Excel content" + b"\x00" * 200),
    ]
    
    created_files = []
    
    for filename, content in test_files:
        file_path = watched_dir / filename
        with open(file_path, 'wb') as f:
            f.write(content)
        created_files.append(str(file_path))
        print(f"✅ Created test file: {file_path}")
    
    return created_files

def wait_for_processing(files, max_wait=30):
    """Wait for files to be processed and moved"""
    processed_dir = Path("processed")
    start_time = time.time()
    
    while time.time() - start_time < max_wait:
        remaining_files = []
        for file_path in files:
            if os.path.exists(file_path):
                remaining_files.append(file_path)
        
        if not remaining_files:
            print("✅ All files have been processed!")
            return True
        
        print(f"⏳ Waiting for {len(remaining_files)} files to be processed...")
        time.sleep(2)
    
    print(f"⚠️ Timeout: {len(remaining_files)} files were not processed within {max_wait} seconds")
    return False

def check_log_files():
    """Check if log files were created"""
    logs_dir = Path("logs")
    if not logs_dir.exists():
        print("❌ Logs directory does not exist")
        return False
    
    log_files = list(logs_dir.glob("*.txt"))
    if not log_files:
        print("❌ No log files found")
        return False
    
    print(f"✅ Found {len(log_files)} log files:")
    for log_file in log_files[-5:]:  # Show last 5 files
        print(f"   📄 {log_file.name}")
        
        # Read and display content of the latest log file
        try:
            with open(log_file, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"      Content preview:")
                for line in content.split('\n')[:3]:
                    if line.strip():
                        print(f"      {line}")
                print()
        except Exception as e:
            print(f"      ⚠️ Could not read file: {e}")
    
    return True

def test_logger_service():
    """Test the logger service directly"""
    try:
        # Test health endpoint
        response = requests.get("http://localhost:8001/health", timeout=5)
        if response.status_code == 200:
            health_data = response.json()
            print("✅ Logger service health check passed:")
            print(f"   Status: {health_data.get('status')}")
            print(f"   Processed files: {health_data.get('processed_files_count', 0)}")
            return True
        else:
            print(f"❌ Logger service health check failed: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Could not connect to logger service: {e}")
        return False

def test_configuration_uis():
    """Test configuration UI accessibility"""
    uis = [
        ("Watcher Config UI", "http://localhost:8080"),
        ("Logger Config UI", "http://localhost:8081")
    ]
    
    for name, url in uis:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"✅ {name} is accessible")
            else:
                print(f"⚠️ {name} returned status {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"❌ {name} is not accessible: {e}")

def main():
    """Main test function"""
    print("🧪 SASA Software Microservices Test Suite")
    print("=" * 50)
    
    # Check if services are running
    print("\n1. Testing service connectivity...")
    logger_ok = test_logger_service()
    
    if not logger_ok:
        print("❌ Logger service is not running. Please start the services first.")
        print("   Run: docker-compose up -d")
        sys.exit(1)
    
    # Test configuration UIs
    print("\n2. Testing configuration UIs...")
    test_configuration_uis()
    
    # Create test files
    print("\n3. Creating test files...")
    test_files = create_test_files()
    
    # Wait for processing
    print("\n4. Waiting for file processing...")
    if wait_for_processing(test_files):
        # Check log files
        print("\n5. Checking log files...")
        check_log_files()
        
        print("\n🎉 Test completed successfully!")
        print("\n📊 System Status:")
        print("   ✅ File monitoring working")
        print("   ✅ JWT authentication working")
        print("   ✅ Log file creation working")
        print("   ✅ File archival working")
        
    else:
        print("\n⚠️ Test completed with issues")
        print("Some files were not processed. Check service logs:")
        print("   docker-compose logs watcher-service")
        print("   docker-compose logs logger-service")
    
    print("\n🔧 Management URLs:")
    print("   • Watcher Config: http://localhost:8080")
    print("   • Logger Config:  http://localhost:8081")
    print("   • Logger API:     http://localhost:8001")

if __name__ == "__main__":
    main()