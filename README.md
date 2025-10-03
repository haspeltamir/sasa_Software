# SASA Software Microservices System

A comprehensive file monitoring and logging system with two microservices that communicate securely using JWT-authenticated HTTP.

## 🎯 Overview

This system monitors a local directory for new files, extracts metadata, securely sends it to a logging service, and processes each file end-to-end with comprehensive configuration management and error handling.

## 🏗️ System Architecture

```
┌─────────────────┐    JWT/HTTP    ┌─────────────────┐
│   Watcher       │◄──────────────►│   Logger        │
│   Service       │                │   Service       │
│   (Port 8000)   │                │   (Port 8001)   │
└─────────────────┘                └─────────────────┘
         │                                   │
         ▼                                   ▼
┌─────────────────┐                ┌─────────────────┐
│   Config UI     │                │   Config UI     │
│   (Port 8080)   │                │   (Port 8081)   │
└─────────────────┘                └─────────────────┘
```

## 🚀 Quick Start

### Option 1: Docker (Recommended)

1. **Prerequisites:**

   - Docker & Docker Compose installed
   - Windows: Use `start.bat`
   - Linux/Mac: Use `start.sh`

2. **Start all services:**

   ```bash
   # Linux/Mac
   chmod +x start.sh
   ./start.sh

   # Windows
   start.bat
   ```

3. **Test the system:**
   - Add a file to the `./watched` directory
   - Check the `./logs` directory for generated log files
   - View service logs: `docker-compose logs -f`

### Option 2: Direct Python

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Start Logger Service:**

   ```bash
   python logger-service/logger.py
   ```

3. **Start Watcher Service:**

   ```bash
   python watcher-service/watcher.py
   ```

4. **Configuration UIs (optional):**

   ```bash
   # Watcher Config UI
   python watcher-service/config_ui.py

   # Logger Config UI
   python logger-service/config_ui.py
   ```

## 📊 Service Endpoints

| Service           | Port | Endpoint  | Description             |
| ----------------- | ---- | --------- | ----------------------- |
| Logger Service    | 8001 | `/log`    | Receive file metadata   |
| Logger Service    | 8001 | `/health` | Health check            |
| Logger Config UI  | 8081 | `/`       | Configuration interface |
| Watcher Config UI | 8080 | `/`       | Configuration interface |

## 🔧 Configuration

Both services include comprehensive configuration management with web-based UIs:

### Watcher Service Configuration

- **Directory Monitoring:** Source, target, and temporary directories
- **File Processing:** Size limits, batch processing, file type filtering
- **JWT Authentication:** Token settings and security
- **Logger Integration:** Service URL, retry policies, timeout settings
- **Notifications:** Email and syslog notifications for errors
- **Logging:** Multi-level logging with rotation

### Logger Service Configuration

- **Server Settings:** Host, port, worker processes
- **Storage Management:** Log directory, retention policies, compression
- **File Processing:** Naming conventions, content templates
- **Validation:** File size limits, filename validation
- **Security:** Rate limiting, CORS, request size limits
- **Notifications:** Error notifications via email/syslog

## 📁 Directory Structure

```
sasa_Software/
├── docker-compose.yml          # Docker orchestration
├── requirements.txt            # Python dependencies
├── start.sh / start.bat       # Startup scripts
├── .env.example               # Environment template
├──
├── shared/                    # Shared utilities
│   ├── jwt_manager.py        # JWT token management
│   └── utils.py              # Common utilities
│
├── watcher-service/           # File monitoring service
│   ├── watcher.py            # Main service
│   ├── config_ui.py          # Configuration UI
│   ├── config.yaml           # Configuration file
│   └── templates/
│       └── config_form.html  # UI template
│
├── logger-service/            # Logging service
│   ├── logger.py             # Main service
│   ├── config_ui.py          # Configuration UI
│   ├── config.yaml           # Configuration file
│   └── templates/
│       └── config_form.html  # UI template
│
├── watched/                   # Monitored directory
├── processed/                 # Successfully processed files
└── logs/                     # Log files and service logs
```

## 🔐 Security Features

### JWT Authentication

- **Algorithm:** HS256
- **Shared Secret:** `sasa-Software2015` (configurable via environment)
- **Token Expiry:** 5 minutes (configurable)
- **Claims Validation:** Issuer and expiration verification

### File Security

- **Filename Sanitization:** Unsafe characters replaced with underscores
- **Size Validation:** Configurable file size limits
- **Path Validation:** Prevents directory traversal attacks

### Network Security

- **Rate Limiting:** Configurable requests per minute
- **CORS Control:** Configurable allowed origins
- **Request Size Limits:** Prevents large payload attacks

## 📝 File Processing Workflow

```
1. File Detection
   └── Watcher monitors ./watched directory

2. Metadata Extraction
   ├── Filename
   ├── Creation timestamp (UTC)
   ├── File size in bytes
   └── SHA256 hash

3. JWT Token Creation
   └── Signed with shared secret

4. HTTP POST to Logger
   ├── Authorization: Bearer <JWT>
   ├── Content-Type: application/json
   └── Body: { filename, created_at, file_size, hash }

5. Log File Creation
   ├── Sanitized filename
   ├── Timestamp format: YYYYMMDDTHHMMSSZ
   └── Pattern: logs/<filename>-<timestamp>.txt

6. File Archival
   └── Move to ./processed directory
```

## 📋 Log File Format

Each processed file generates a log entry with the following format:

```
Filename: example.pdf
Size: 1.2MB
Created At: 2025-09-30T14:33:22Z
Hash: sha256_hash_here
Processed At: 2025-09-30T14:33:25Z
```

## 🔔 Notification System

### Email Notifications

- **SMTP Support:** Gmail, Outlook, custom SMTP servers
- **TLS/SSL:** Secure email transmission
- **Multiple Recipients:** Comma-separated email lists
- **Error Alerts:** Automatic error notifications

### Syslog Integration

- **Standard Facilities:** LOG_USER, LOG_LOCAL0-7
- **Multiple Levels:** DEBUG, INFO, WARNING, ERROR, CRITICAL
- **System Integration:** Works with rsyslog, syslog-ng

## 📊 Monitoring & Health Checks

### Health Endpoints

- **Logger Service:** `GET /health` - Service status and statistics
- **Docker Health Checks:** Automatic container health monitoring
- **Uptime Tracking:** Service start time and processed file counts

### Logging Levels

- **DEBUG:** Detailed processing information
- **INFO:** Normal operations and file processing
- **WARNING:** Non-critical issues and retries
- **ERROR:** Processing failures and exceptions
- **CRITICAL:** Service failures and system errors

## 🐳 Docker Configuration

### Environment Variables

```bash
# JWT Configuration
JWT_SECRET=sasa-Software2015

# Email Configuration
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password

# Logging
LOG_LEVEL=INFO
```

### Volume Mounts

- `./watched:/app/watched` - File monitoring directory
- `./processed:/app/processed` - Processed files archive
- `./logs:/app/logs` - Log files and service logs
- `./config.yaml:/app/config.yaml` - Service configuration

## 🛠️ Development & Customization

### Adding New Features

1. **Extend Configuration:** Add new settings to `config.yaml`
2. **Update UI:** Modify template files for configuration forms
3. **Implement Logic:** Add processing in service files
4. **Test Integration:** Verify with Docker compose

### Custom Notification Methods

1. **Extend NotificationHandler:** Add new methods in `shared/utils.py`
2. **Update Configuration:** Add settings for new notification types
3. **Integration:** Call new methods in error handling

### File Processing Extensions

1. **Custom Metadata:** Extend metadata extraction in FileProcessor
2. **Content Analysis:** Add file content inspection
3. **Format Support:** Add support for specific file types

## 🔍 Troubleshooting

### Common Issues

**Services won't start:**

- Check Docker installation
- Verify port availability (8000, 8001, 8080, 8081)
- Review Docker logs: `docker-compose logs`

**JWT Authentication Failures:**

- Verify shared secret matches in both services
- Check token expiration settings
- Ensure system clocks are synchronized

**File Processing Issues:**

- Check directory permissions
- Verify file size limits
- Review exclude patterns in configuration

**Email Notifications Not Working:**

- Verify SMTP settings
- Check app passwords for Gmail
- Test SMTP connectivity

### Log Analysis

```bash
# View all service logs
docker-compose logs -f

# View specific service logs
docker-compose logs -f watcher-service
docker-compose logs -f logger-service

# View service logs from files
tail -f logs/watcher-service.log
tail -f logs/logger-service.log
```

## 📈 Performance Considerations

### Scalability

- **Horizontal Scaling:** Multiple watcher instances can send to single logger
- **Load Balancing:** Logger service supports multiple workers
- **Batch Processing:** Configurable batch sizes for high-volume scenarios

### Resource Management

- **Memory Usage:** Log rotation prevents disk space issues
- **CPU Optimization:** Configurable polling intervals
- **Network Efficiency:** Retry policies and timeout configurations

## 🔒 Security Best Practices

1. **Change Default Secrets:** Update JWT secret in production
2. **Use Environment Variables:** Store sensitive configuration in .env
3. **Network Isolation:** Use Docker networks for service communication
4. **Regular Updates:** Keep dependencies updated
5. **Monitor Logs:** Watch for authentication failures and errors

## 📄 License

This project is part of the SASA Software suite and is proprietary software.

## 🤝 Support

For support and maintenance:

- Review service logs for error details
- Use configuration UIs for easy management
- Check Docker container health status
- Monitor system resources and performance

## 🔄 Version History

- **v1.0.0:** Initial release with core functionality
  - JWT-authenticated file monitoring
  - Web-based configuration management
  - Docker containerization
  - Comprehensive error handling and notifications
