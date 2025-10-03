@echo off
echo 🚀 Starting SASA Software Microservices...

REM Check if Docker is installed
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker is not installed. Please install Docker first.
    exit /b 1
)

docker-compose --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker Compose is not installed. Please install Docker Compose first.
    exit /b 1
)

REM Check if .env file exists, if not create from example
if not exist .env (
    echo 📝 Creating .env file from example...
    copy .env.example .env
    echo ✅ Please edit .env file with your configuration before running again.
    exit /b 1
)

REM Create directories if they don't exist
if not exist watched mkdir watched
if not exist processed mkdir processed
if not exist logs mkdir logs
if not exist temp mkdir temp

REM Stop any existing containers
echo 🛑 Stopping existing containers...
docker-compose down

REM Build and start services
echo 🔨 Building and starting services...
docker-compose up --build -d

REM Wait for services to start
echo ⏳ Waiting for services to start...
timeout /t 10 /nobreak >nul

REM Check service status
echo 🔍 Checking service status...

REM Check Logger Service
curl -s http://localhost:8001/health >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Logger Service is running on http://localhost:8001
) else (
    echo ❌ Logger Service failed to start
)

REM Check Configuration UIs
curl -s http://localhost:8080/ >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Watcher Config UI is running on http://localhost:8080
) else (
    echo ❌ Watcher Config UI failed to start
)

curl -s http://localhost:8081/ >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Logger Config UI is running on http://localhost:8081
) else (
    echo ❌ Logger Config UI failed to start
)

echo.
echo 🎉 SASA Software Microservices are now running!
echo.
echo 📊 Service Endpoints:
echo    • Logger Service:      http://localhost:8001
echo    • Logger Config UI:    http://localhost:8081
echo    • Watcher Config UI:   http://localhost:8080
echo.
echo 📁 Directories:
echo    • Watched:    .\watched
echo    • Processed:  .\processed
echo    • Logs:       .\logs
echo.
echo 🔧 Management Commands:
echo    • View logs:     docker-compose logs -f
echo    • Stop services: docker-compose down
echo    • Restart:       docker-compose restart
echo.
echo 💡 To test the system, add a file to the '.\watched' directory.

pause