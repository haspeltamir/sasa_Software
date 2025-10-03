# SASA Software Microservices Startup Script for PowerShell
# Run this script to start all services

Write-Host "🚀 Starting SASA Software Microservices..." -ForegroundColor Green

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python found: $pythonVersion" -ForegroundColor Green
}
catch {
    Write-Host "❌ Python is not installed or not in PATH. Please install Python first." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Install requirements
Write-Host "📦 Installing Python dependencies..." -ForegroundColor Yellow
try {
    pip install -r requirements.txt
    if ($LASTEXITCODE -ne 0) {
        throw "pip install failed"
    }
    Write-Host "✅ Dependencies installed successfully" -ForegroundColor Green
}
catch {
    Write-Host "❌ Failed to install dependencies. Please check the error above." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Create directories if they don't exist
$directories = @("watched", "processed", "logs", "temp")
foreach ($dir in $directories) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir | Out-Null
        Write-Host "📁 Created directory: $dir" -ForegroundColor Cyan
    }
}

# Start Logger Service in background
Write-Host "🔧 Starting Logger Service..." -ForegroundColor Yellow
$loggerJob = Start-Job -ScriptBlock { 
    Set-Location $using:PWD
    python logger-service/logger.py 
}

# Wait a moment for logger to start
Start-Sleep -Seconds 3

# Check if logger started successfully
Write-Host "🔍 Checking Logger Service..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8001/health" -TimeoutSec 5 -ErrorAction Stop
    Write-Host "✅ Logger Service is running" -ForegroundColor Green
}
catch {
    Write-Host "⚠️ Logger Service may not be ready yet" -ForegroundColor Yellow
}

# Display service information
Write-Host ""
Write-Host "📊 Service Information:" -ForegroundColor Cyan
Write-Host "   • Logger Service:      http://localhost:8001" -ForegroundColor White
Write-Host "   • Logger Config UI:    http://localhost:8081" -ForegroundColor White
Write-Host "   • Watcher Config UI:   http://localhost:8080" -ForegroundColor White
Write-Host ""
Write-Host "📁 Directories:" -ForegroundColor Cyan
Write-Host "   • Watched:    .\watched" -ForegroundColor White
Write-Host "   • Processed:  .\processed" -ForegroundColor White
Write-Host "   • Logs:       .\logs" -ForegroundColor White
Write-Host ""
Write-Host "💡 To test the system, add a file to the '.\watched' directory." -ForegroundColor Yellow
Write-Host "🛑 Press Ctrl+C to stop the services." -ForegroundColor Red
Write-Host ""

# Start Watcher Service (foreground)
Write-Host "👁️ Starting Watcher Service..." -ForegroundColor Yellow
try {
    python watcher-service/watcher.py
}
catch {
    Write-Host "❌ Watcher Service failed to start" -ForegroundColor Red
}
finally {
    # Clean up background job when script exits
    Write-Host "🛑 Stopping Logger Service..." -ForegroundColor Yellow
    Stop-Job $loggerJob -ErrorAction SilentlyContinue
    Remove-Job $loggerJob -ErrorAction SilentlyContinue
}