#!/bin/bash

# SASA Software Microservices Startup Script
# Run this script to start all services

echo "🚀 Starting SASA Software Microservices..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Check if .env file exists, if not create from example
if [ ! -f .env ]; then
    echo "📝 Creating .env file from example..."
    cp .env.example .env
    echo "✅ Please edit .env file with your configuration before running again."
    exit 1
fi

# Create directories if they don't exist
mkdir -p watched processed logs temp

# Stop any existing containers
echo "🛑 Stopping existing containers..."
docker-compose down

# Build and start services
echo "🔨 Building and starting services..."
docker-compose up --build -d

# Wait for services to start
echo "⏳ Waiting for services to start..."
sleep 10

# Check service status
echo "🔍 Checking service status..."

# Check Logger Service
if curl -s http://localhost:8001/health > /dev/null; then
    echo "✅ Logger Service is running on http://localhost:8001"
else
    echo "❌ Logger Service failed to start"
fi

# Check Watcher Service (health endpoint)
if curl -s http://localhost:8000/health > /dev/null; then
    echo "✅ Watcher Service is running"
else
    echo "❌ Watcher Service failed to start"
fi

# Check Configuration UIs
if curl -s http://localhost:8080/ > /dev/null; then
    echo "✅ Watcher Config UI is running on http://localhost:8080"
else
    echo "❌ Watcher Config UI failed to start"
fi

if curl -s http://localhost:8081/ > /dev/null; then
    echo "✅ Logger Config UI is running on http://localhost:8081"
else
    echo "❌ Logger Config UI failed to start"
fi

echo ""
echo "🎉 SASA Software Microservices are now running!"
echo ""
echo "📊 Service Endpoints:"
echo "   • Logger Service:      http://localhost:8001"
echo "   • Logger Config UI:    http://localhost:8081"
echo "   • Watcher Config UI:   http://localhost:8080"
echo ""
echo "📁 Directories:"
echo "   • Watched:    ./watched"
echo "   • Processed:  ./processed"
echo "   • Logs:       ./logs"
echo ""
echo "🔧 Management Commands:"
echo "   • View logs:     docker-compose logs -f"
echo "   • Stop services: docker-compose down"
echo "   • Restart:       docker-compose restart"
echo ""
echo "💡 To test the system, add a file to the './watched' directory."