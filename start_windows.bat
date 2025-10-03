@echo off
REM SASA Software Microservices Startup Script for Windows
REM Run this script to start all services

echo 🚀 Starting SASA Software Microservices...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH. Please install Python first.
    pause
    exit /b 1
)

REM Install requirements if needed
echo 📦 Installing Python dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Failed to install dependencies. Please check the error above.
    pause
    exit /b 1
)

REM Create directories if they don't exist
if not exist "watched" mkdir watched
if not exist "processed" mkdir processed
if not exist "logs" mkdir logs
if not exist "temp" mkdir temp

echo 📁 Created required directories

REM Start Logger Service in background
echo 🔧 Starting Logger Service...
start "Logger Service" /min cmd /c "python logger-service/logger.py"

REM Wait a moment for logger to start
timeout /t 3 /nobreak >nul

REM Start Watcher Service
echo 👁️ Starting Watcher Service...
echo.
echo 📊 Service Information:
echo    • Logger Service:      http://localhost:8001
echo    • Logger Config UI:    http://localhost:8081
echo    • Watcher Config UI:   http://localhost:8080
echo.
echo 📁 Directories:
echo    • Watched:    .\watched
echo    • Processed:  .\processed
echo    • Logs:       .\logs
echo.
echo 💡 To test the system, add a file to the '.\watched' directory.
echo 🛑 Press Ctrl+C to stop the watcher service.
echo.

python watcher-service/watcher.py