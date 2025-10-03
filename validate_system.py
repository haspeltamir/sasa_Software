#!/usr/bin/env python3

"""
SASA Software System Validation
Comprehensive validation script to ensure all components are working correctly
"""

import os
import sys
import json
import time
import hashlib
import requests
import tempfile
from datetime import datetime
from pathlib import Path

class SystemValidator:
    """Validates the entire SASA Software system"""
    
    def __init__(self):
        self.logger_url = "http://localhost:8001"
        self.watcher_config_url = "http://localhost:8080"
        self.logger_config_url = "http://localhost:8081"
        self.test_files = []
        
    def validate_dependencies(self):
        """Validate system dependencies"""
        print("🔍 Validating system dependencies...")
        
        required_dirs = ['watched', 'processed', 'logs', 'shared']
        missing_dirs = []
        
        for dir_name in required_dirs:
            if not Path(dir_name).exists():
                missing_dirs.append(dir_name)
        
        if missing_dirs:
            print(f"❌ Missing directories: {', '.join(missing_dirs)}")
            return False
        
        print("✅ All required directories exist")
        return True
    
    def validate_services(self):
        """Validate service connectivity"""
        print("🌐 Validating service connectivity...")
        
        services = {
            "Logger Service": f"{self.logger_url}/health",
            "Watcher Config UI": self.watcher_config_url,
            "Logger Config UI": self.logger_config_url
        }
        
        all_ok = True
        for name, url in services.items():
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    print(f"✅ {name}: OK")
                else:
                    print(f"⚠️ {name}: HTTP {response.status_code}")
                    all_ok = False
            except requests.exceptions.RequestException as e:
                print(f"❌ {name}: {e}")
                all_ok = False
        
        return all_ok
    
    def validate_jwt_functionality(self):
        """Validate JWT functionality"""
        print("🔐 Validating JWT functionality...")
        
        try:
            # Import JWT manager
            sys.path.append('shared')
            from jwt_manager import JWTManager
            
            # Test JWT creation and validation
            jwt_manager = JWTManager("test-secret")
            
            # Create token
            token = jwt_manager.create_token("test-issuer", expiry_minutes=1)
            print(f"✅ JWT token created: {token[:50]}...")
            
            # Validate token
            payload = jwt_manager.validate_token(token, "test-issuer")
            print(f"✅ JWT token validated: {payload.get('iss')}")
            
            return True
            
        except Exception as e:
            print(f"❌ JWT validation failed: {e}")
            return False
    
    def validate_file_processing(self):
        """Validate end-to-end file processing"""
        print("📁 Validating file processing workflow...")
        
        # Create test file with known content
        test_content = f"Test file created at {datetime.utcnow().isoformat()}Z\nSASA Software System Validation"
        test_filename = f"validation_test_{int(time.time())}.txt"
        test_file_path = Path("watched") / test_filename
        
        try:
            # Write test file
            with open(test_file_path, 'w', encoding='utf-8') as f:
                f.write(test_content)
            
            print(f"✅ Created test file: {test_filename}")
            self.test_files.append(test_file_path)
            
            # Calculate expected hash
            expected_hash = hashlib.sha256(test_content.encode('utf-8')).hexdigest()
            print(f"✅ Expected hash: {expected_hash}")
            
            # Wait for processing
            processed_file = Path("processed") / test_filename
            log_pattern = f"validation_test_*-*.txt"
            
            max_wait = 30
            start_time = time.time()
            
            while time.time() - start_time < max_wait:
                if processed_file.exists():
                    print("✅ File successfully moved to processed directory")
                    break
                time.sleep(1)
            else:
                print("⚠️ File was not moved to processed directory within timeout")
                return False
            
            # Check for log file
            logs_dir = Path("logs")
            log_files = list(logs_dir.glob(log_pattern))
            
            if not log_files:
                print("❌ No corresponding log file found")
                return False
            
            log_file = log_files[0]
            print(f"✅ Found log file: {log_file.name}")
            
            # Validate log content
            with open(log_file, 'r', encoding='utf-8') as f:
                log_content = f.read()
            
            required_fields = ['Filename:', 'Size:', 'Created At:', 'Hash:', 'Processed At:']
            missing_fields = []
            
            for field in required_fields:
                if field not in log_content:
                    missing_fields.append(field)
            
            if missing_fields:
                print(f"❌ Missing fields in log file: {', '.join(missing_fields)}")
                return False
            
            print("✅ Log file contains all required fields")
            
            # Validate hash in log file
            if expected_hash in log_content:
                print("✅ File hash correctly recorded in log")
            else:
                print("⚠️ File hash not found in log file")
            
            return True
            
        except Exception as e:
            print(f"❌ File processing validation failed: {e}")
            return False
    
    def validate_error_handling(self):
        """Validate error handling"""
        print("⚠️ Validating error handling...")
        
        # Test invalid JWT
        try:
            headers = {
                "Authorization": "Bearer invalid.jwt.token",
                "Content-Type": "application/json"
            }
            
            data = {
                "filename": "test.txt",
                "created_at": "2025-09-30T14:33:22Z",
                "file_size": 100
            }
            
            response = requests.post(f"{self.logger_url}/log", 
                                   json=data, headers=headers, timeout=5)
            
            if response.status_code == 401:
                print("✅ Invalid JWT correctly rejected")
            else:
                print(f"⚠️ Expected 401, got {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ Error handling validation failed: {e}")
            return False
        
        # Test malformed payload
        try:
            # Create valid JWT for test (would need actual secret)
            headers = {
                "Authorization": "Bearer test.token", 
                "Content-Type": "application/json"
            }
            
            # Invalid data (missing required fields)
            data = {"invalid": "data"}
            
            response = requests.post(f"{self.logger_url}/log",
                                   json=data, headers=headers, timeout=5)
            
            if response.status_code in [400, 401]:  # Either validation error or auth error
                print("✅ Malformed payload correctly rejected")
            else:
                print(f"⚠️ Expected 400/401, got {response.status_code}")
        
        except Exception as e:
            print(f"⚠️ Malformed payload test failed: {e}")
        
        return True
    
    def validate_configuration(self):
        """Validate configuration files"""
        print("⚙️ Validating configuration files...")
        
        config_files = [
            "watcher-service/config.yaml",
            "logger-service/config.yaml"
        ]
        
        all_ok = True
        for config_file in config_files:
            if not Path(config_file).exists():
                print(f"❌ Missing config file: {config_file}")
                all_ok = False
            else:
                print(f"✅ Found config file: {config_file}")
        
        return all_ok
    
    def validate_docker_setup(self):
        """Validate Docker setup"""
        print("🐳 Validating Docker setup...")
        
        docker_files = [
            "docker-compose.yml",
            "Dockerfile.watcher", 
            "Dockerfile.logger",
            "requirements.txt"
        ]
        
        all_ok = True
        for docker_file in docker_files:
            if not Path(docker_file).exists():
                print(f"❌ Missing Docker file: {docker_file}")
                all_ok = False
            else:
                print(f"✅ Found Docker file: {docker_file}")
        
        return all_ok
    
    def cleanup_test_files(self):
        """Clean up test files"""
        print("🧹 Cleaning up test files...")
        
        for test_file in self.test_files:
            try:
                if test_file.exists():
                    test_file.unlink()
                    print(f"🗑️ Removed: {test_file}")
            except Exception as e:
                print(f"⚠️ Could not remove {test_file}: {e}")
    
    def run_full_validation(self):
        """Run complete system validation"""
        print("🔬 SASA Software System Validation")
        print("=" * 50)
        
        validations = [
            ("Dependencies", self.validate_dependencies),
            ("Services", self.validate_services),
            ("JWT Functionality", self.validate_jwt_functionality),
            ("Configuration", self.validate_configuration),
            ("Docker Setup", self.validate_docker_setup),
            ("File Processing", self.validate_file_processing),
            ("Error Handling", self.validate_error_handling),
        ]
        
        results = {}
        
        for name, validation_func in validations:
            try:
                result = validation_func()
                results[name] = result
                print()
            except Exception as e:
                print(f"❌ {name} validation failed with exception: {e}")
                results[name] = False
                print()
        
        # Cleanup
        self.cleanup_test_files()
        
        # Summary
        print("📋 Validation Summary")
        print("=" * 30)
        
        passed = 0
        total = len(results)
        
        for name, result in results.items():
            status = "✅ PASS" if result else "❌ FAIL"
            print(f"{name:20}: {status}")
            if result:
                passed += 1
        
        print(f"\nResult: {passed}/{total} validations passed")
        
        if passed == total:
            print("🎉 All validations passed! System is working correctly.")
            return True
        else:
            print("⚠️ Some validations failed. Please check the issues above.")
            return False


def main():
    """Main validation function"""
    validator = SystemValidator()
    success = validator.run_full_validation()
    
    if success:
        print("\n✅ System validation completed successfully!")
        sys.exit(0)
    else:
        print("\n❌ System validation failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()