<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SASA Software Microservices System - Complete Documentation</title>
    <style>
        @media print {
            .page-break { page-break-before: always; }
            .no-print { display: none; }
        }
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            line-height: 1.6; 
            margin: 20px;
            background: white;
        }
        .bilingual-container {
            display: flex;
            gap: 20px;
            margin: 20px 0;
        }
        .english-section {
            flex: 1;
            border-left: 4px solid #007bff;
            padding-left: 15px;
        }
        .hebrew-section {
            flex: 1;
            border-right: 4px solid #28a745;
            padding-right: 15px;
            direction: rtl;
            text-align: right;
        }
        .toc-entry {
            margin: 8px 0;
            padding: 5px 0;
        }
        .toc-level-1 {
            font-size: 18px;
            font-weight: bold;
            color: #333;
            margin-top: 20px;
        }
        .toc-level-2 {
            font-size: 16px;
            font-weight: 600;
            color: #555;
            margin-left: 20px;
            margin-right: 20px;
        }
        .toc-level-3 {
            font-size: 14px;
            color: #666;
            margin-left: 40px;
            margin-right: 40px;
        }
        .page-number {
            float: right;
            color: #888;
        }
        .page-number-hebrew {
            float: left;
            color: #888;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        .cover-title {
            text-align: center;
            font-size: 3em;
            margin: 100px 0 50px 0;
            color: #2c3e50;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        .cover-subtitle {
            text-align: center;
            font-size: 1.5em;
            color: #7f8c8d;
            margin-bottom: 50px;
        }
        .cover-date {
            text-align: center;
            font-size: 1.2em;
            color: #95a5a6;
        }
        .architecture-diagram {
            text-align: center;
            margin: 30px 0;
        }
    </style>
</head>
<body>

<!-- COVER PAGE -->
<div class="page-break">
<div class="cover-title">
    📊 SASA SOFTWARE<br>
    MICROSERVICES SYSTEM
</div>

<div class="cover-subtitle">
    Complete Technical Documentation Guide<br>
    מדריך תיעוד טכני מלא
</div>

<div class="architecture-diagram">
    <pre style="font-family: monospace; font-size: 14px; line-height: 1.2;">
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
    </pre>
</div>

<div class="cover-date">
    <strong>Version:</strong> 1.0.0<br>
    <strong>Date:</strong> October 3, 2025<br>
    <strong>Author:</strong> SASA Software Development Team
</div>
</div>

<!-- TABLE OF CONTENTS -->
<div class="page-break">
<h1 style="text-align: center; border-bottom: 3px solid #3498db; padding-bottom: 20px;">
    📋 TABLE OF CONTENTS / תוכן עניינים
</h1>

<div class="bilingual-container">
    
<!-- ENGLISH TABLE OF CONTENTS -->
<div class="english-section">
<h2>📖 English Contents</h2>

<div class="toc-entry toc-level-1">
    <strong>1. Project Overview & Introduction</strong>
    <span class="page-number">Page 5</span>
    <div class="toc-entry toc-level-2">
        1.1 System Architecture Overview <span class="page-number">Page 6</span>
    </div>
    <div class="toc-entry toc-level-2">
        1.2 Technology Stack & Dependencies <span class="page-number">Page 7</span>
    </div>
    <div class="toc-entry toc-level-2">
        1.3 Security & Authentication Flow <span class="page-number">Page 8</span>
    </div>
</div>

<div class="toc-entry toc-level-1">
    <strong>2. Quick Start Guide</strong>
    <span class="page-number">Page 10</span>
    <div class="toc-entry toc-level-2">
        2.1 Prerequisites & Installation <span class="page-number">Page 11</span>
    </div>
    <div class="toc-entry toc-level-2">
        2.2 Docker Deployment Method <span class="page-number">Page 12</span>
    </div>
    <div class="toc-entry toc-level-2">
        2.3 Python Direct Execution Method <span class="page-number">Page 13</span>
    </div>
    <div class="toc-entry toc-level-2">
        2.4 First System Test & Verification <span class="page-number">Page 14</span>
    </div>
</div>

<div class="toc-entry toc-level-1">
    <strong>3. Project Structure Deep Dive</strong>
    <span class="page-number">Page 16</span>
    <div class="toc-entry toc-level-2">
        3.1 Root Directory Files Analysis <span class="page-number">Page 17</span>
        <div class="toc-entry toc-level-3">
            3.1.1 docker-compose.yml - Container Orchestration <span class="page-number">Page 18</span>
        </div>
        <div class="toc-entry toc-level-3">
            3.1.2 requirements.txt - Python Dependencies <span class="page-number">Page 19</span>
        </div>
        <div class="toc-entry toc-level-3">
            3.1.3 manage.py - System Management Script <span class="page-number">Page 20</span>
        </div>
        <div class="toc-entry toc-level-3">
            3.1.4 Startup Scripts (start.bat, start.sh, start.ps1) <span class="page-number">Page 21</span>
        </div>
    </div>
</div>

<div class="toc-entry toc-level-1">
    <strong>4. Shared Components</strong>
    <span class="page-number">Page 23</span>
    <div class="toc-entry toc-level-2">
        4.1 shared/utils.py - Common Utilities <span class="page-number">Page 24</span>
        <div class="toc-entry toc-level-3">
            4.1.1 ConfigManager Class - Line by Line <span class="page-number">Page 25</span>
        </div>
        <div class="toc-entry toc-level-3">
            4.1.2 NotificationHandler Class - Email & Syslog <span class="page-number">Page 26</span>
        </div>
        <div class="toc-entry toc-level-3">
            4.1.3 Logging Setup Functions <span class="page-number">Page 27</span>
        </div>
    </div>
    <div class="toc-entry toc-level-2">
        4.2 shared/jwt_manager.py - JWT Authentication <span class="page-number">Page 28</span>
        <div class="toc-entry toc-level-3">
            4.2.1 Token Creation Functions <span class="page-number">Page 29</span>
        </div>
        <div class="toc-entry toc-level-3">
            4.2.2 Token Validation & Security <span class="page-number">Page 30</span>
        </div>
    </div>
</div>

<div class="toc-entry toc-level-1">
    <strong>5. Watcher Service Complete Analysis</strong>
    <span class="page-number">Page 32</span>
    <div class="toc-entry toc-level-2">
        5.1 watcher-service/watcher.py - Main Service <span class="page-number">Page 33</span>
        <div class="toc-entry toc-level-3">
            5.1.1 Import Statements & Dependencies <span class="page-number">Page 34</span>
        </div>
        <div class="toc-entry toc-level-3">
            5.1.2 FileProcessor Class - Complete Breakdown <span class="page-number">Page 35</span>
        </div>
        <div class="toc-entry toc-level-3">
            5.1.3 WatcherEventHandler Class - File Events <span class="page-number">Page 38</span>
        </div>
        <div class="toc-entry toc-level-3">
            5.1.4 WatcherService Class - Main Logic <span class="page-number">Page 40</span>
        </div>
        <div class="toc-entry toc-level-3">
            5.1.5 Main Function & Service Startup <span class="page-number">Page 42</span>
        </div>
    </div>
    <div class="toc-entry toc-level-2">
        5.2 watcher-service/config_ui.py - Configuration Interface <span class="page-number">Page 44</span>
    </div>
    <div class="toc-entry toc-level-2">
        5.3 watcher-service/config.yaml - Configuration File <span class="page-number">Page 46</span>
    </div>
    <div class="toc-entry toc-level-2">
        5.4 watcher-service/templates/config_form.html - Web UI <span class="page-number">Page 48</span>
    </div>
</div>

<div class="toc-entry toc-level-1">
    <strong>6. Logger Service Complete Analysis</strong>
    <span class="page-number">Page 50</span>
    <div class="toc-entry toc-level-2">
        6.1 logger-service/logger.py - Main Service <span class="page-number">Page 51</span>
        <div class="toc-entry toc-level-3">
            6.1.1 Pydantic Models - Data Validation <span class="page-number">Page 52</span>
        </div>
        <div class="toc-entry toc-level-3">
            6.1.2 LoggerService Class - Core Logic <span class="page-number">Page 54</span>
        </div>
        <div class="toc-entry toc-level-3">
            6.1.3 FastAPI Endpoints - HTTP Handlers <span class="page-number">Page 56</span>
        </div>
        <div class="toc-entry toc-level-3">
            6.1.4 Log File Creation & Management <span class="page-number">Page 58</span>
        </div>
    </div>
    <div class="toc-entry toc-level-2">
        6.2 logger-service/config_ui.py - Configuration Interface <span class="page-number">Page 60</span>
    </div>
    <div class="toc-entry toc-level-2">
        6.3 logger-service/config.yaml - Configuration File <span class="page-number">Page 62</span>
    </div>
    <div class="toc-entry toc-level-2">
        6.4 logger-service/templates/config_form.html - Web UI <span class="page-number">Page 64</span>
    </div>
</div>

<div class="toc-entry toc-level-1">
    <strong>7. Docker Configuration</strong>
    <span class="page-number">Page 66</span>
    <div class="toc-entry toc-level-2">
        7.1 Dockerfile.watcher - Watcher Container <span class="page-number">Page 67</span>
    </div>
    <div class="toc-entry toc-level-2">
        7.2 Dockerfile.logger - Logger Container <span class="page-number">Page 68</span>
    </div>
    <div class="toc-entry toc-level-2">
        7.3 docker-compose.yml - Orchestration <span class="page-number">Page 69</span>
    </div>
</div>

<div class="toc-entry toc-level-1">
    <strong>8. Testing & Validation</strong>
    <span class="page-number">Page 71</span>
    <div class="toc-entry toc-level-2">
        8.1 test_system.py - Automated Testing <span class="page-number">Page 72</span>
    </div>
    <div class="toc-entry toc-level-2">
        8.2 validate_system.py - System Validation <span class="page-number">Page 74</span>
    </div>
    <div class="toc-entry toc-level-2">
        8.3 Manual Testing Procedures <span class="page-number">Page 76</span>
    </div>
</div>

<div class="toc-entry toc-level-1">
    <strong>9. Configuration Management</strong>
    <span class="page-number">Page 78</span>
    <div class="toc-entry toc-level-2">
        9.1 YAML Configuration Structure <span class="page-number">Page 79</span>
    </div>
    <div class="toc-entry toc-level-2">
        9.2 Environment Variables <span class="page-number">Page 80</span>
    </div>
    <div class="toc-entry toc-level-2">
        9.3 Web-based Configuration UIs <span class="page-number">Page 81</span>
    </div>
</div>

<div class="toc-entry toc-level-1">
    <strong>10. Security & Authentication</strong>
    <span class="page-number">Page 83</span>
    <div class="toc-entry toc-level-2">
        10.1 JWT Token Lifecycle <span class="page-number">Page 84</span>
    </div>
    <div class="toc-entry toc-level-2">
        10.2 File Security & Validation <span class="page-number">Page 85</span>
    </div>
    <div class="toc-entry toc-level-2">
        10.3 Network Security <span class="page-number">Page 86</span>
    </div>
</div>

<div class="toc-entry toc-level-1">
    <strong>11. Monitoring & Logging</strong>
    <span class="page-number">Page 88</span>
    <div class="toc-entry toc-level-2">
        11.1 Service Logs Analysis <span class="page-number">Page 89</span>
    </div>
    <div class="toc-entry toc-level-2">
        11.2 Health Check Endpoints <span class="page-number">Page 90</span>
    </div>
    <div class="toc-entry toc-level-2">
        11.3 Error Notification Systems <span class="page-number">Page 91</span>
    </div>
</div>

<div class="toc-entry toc-level-1">
    <strong>12. Troubleshooting Guide</strong>
    <span class="page-number">Page 93</span>
    <div class="toc-entry toc-level-2">
        12.1 Common Issues & Solutions <span class="page-number">Page 94</span>
    </div>
    <div class="toc-entry toc-level-2">
        12.2 Debug Mode & Advanced Logging <span class="page-number">Page 96</span>
    </div>
    <div class="toc-entry toc-level-2">
        12.3 Performance Optimization <span class="page-number">Page 98</span>
    </div>
</div>

<div class="toc-entry toc-level-1">
    <strong>13. API Reference</strong>
    <span class="page-number">Page 100</span>
    <div class="toc-entry toc-level-2">
        13.1 Logger Service API <span class="page-number">Page 101</span>
    </div>
    <div class="toc-entry toc-level-2">
        13.2 Configuration API <span class="page-number">Page 103</span>
    </div>
    <div class="toc-entry toc-level-2">
        13.3 HTTP Status Codes & Error Handling <span class="page-number">Page 105</span>
    </div>
</div>

<div class="toc-entry toc-level-1">
    <strong>14. Appendices</strong>
    <span class="page-number">Page 107</span>
    <div class="toc-entry toc-level-2">
        14.1 Complete Code Listings <span class="page-number">Page 108</span>
    </div>
    <div class="toc-entry toc-level-2">
        14.2 Configuration Templates <span class="page-number">Page 115</span>
    </div>
    <div class="toc-entry toc-level-2">
        14.3 Glossary & Technical Terms <span class="page-number">Page 120</span>
    </div>
</div>

</div>

<!-- HEBREW TABLE OF CONTENTS -->
<div class="hebrew-section">
<h2>📖 תוכן עניינים בעברית</h2>

<div class="toc-entry toc-level-1">
    <strong>1. סקירת פרויקט ומבוא</strong>
    <span class="page-number-hebrew">עמוד 5</span>
    <div class="toc-entry toc-level-2">
        1.1 סקירת ארכיטקטורת המערכת <span class="page-number-hebrew">עמוד 6</span>
    </div>
    <div class="toc-entry toc-level-2">
        1.2 מחסנית טכנולוגיות ותלויות <span class="page-number-hebrew">עמוד 7</span>
    </div>
    <div class="toc-entry toc-level-2">
        1.3 אבטחה וזרימת אימות <span class="page-number-hebrew">עמוד 8</span>
    </div>
</div>

<div class="toc-entry toc-level-1">
    <strong>2. מדריך התחלה מהירה</strong>
    <span class="page-number-hebrew">עמוד 10</span>
    <div class="toc-entry toc-level-2">
        2.1 דרישות מוקדמות והתקנה <span class="page-number-hebrew">עמוד 11</span>
    </div>
    <div class="toc-entry toc-level-2">
        2.2 שיטת פריסה עם Docker <span class="page-number-hebrew">עמוד 12</span>
    </div>
    <div class="toc-entry toc-level-2">
        2.3 שיטת הרצה ישירה עם Python <span class="page-number-hebrew">עמוד 13</span>
    </div>
    <div class="toc-entry toc-level-2">
        2.4 בדיקה ראשונה של המערכת ואימות <span class="page-number-hebrew">עמוד 14</span>
    </div>
</div>

<div class="toc-entry toc-level-1">
    <strong>3. ניתוח מעמיק של מבנה הפרויקט</strong>
    <span class="page-number-hebrew">עמוד 16</span>
    <div class="toc-entry toc-level-2">
        3.1 ניתוח קבצי תיקיית השורש <span class="page-number-hebrew">עמוד 17</span>
        <div class="toc-entry toc-level-3">
            3.1.1 docker-compose.yml - תזמור מכולות <span class="page-number-hebrew">עמוד 18</span>
        </div>
        <div class="toc-entry toc-level-3">
            3.1.2 requirements.txt - תלויות Python <span class="page-number-hebrew">עמוד 19</span>
        </div>
        <div class="toc-entry toc-level-3">
            3.1.3 manage.py - סקריפט ניהול מערכת <span class="page-number-hebrew">עמוד 20</span>
        </div>
        <div class="toc-entry toc-level-3">
            3.1.4 סקריפטי הפעלה (start.bat, start.sh, start.ps1) <span class="page-number-hebrew">עמוד 21</span>
        </div>
    </div>
</div>

<div class="toc-entry toc-level-1">
    <strong>4. רכיבים משותפים</strong>
    <span class="page-number-hebrew">עמוד 23</span>
    <div class="toc-entry toc-level-2">
        4.1 shared/utils.py - כלי עזר משותפים <span class="page-number-hebrew">עמוד 24</span>
        <div class="toc-entry toc-level-3">
            4.1.1 מחלקת ConfigManager - שורה אחר שורה <span class="page-number-hebrew">עמוד 25</span>
        </div>
        <div class="toc-entry toc-level-3">
            4.1.2 מחלקת NotificationHandler - אימייל ו-Syslog <span class="page-number-hebrew">עמוד 26</span>
        </div>
        <div class="toc-entry toc-level-3">
            4.1.3 פונקציות הגדרת רישום <span class="page-number-hebrew">עמוד 27</span>
        </div>
    </div>
    <div class="toc-entry toc-level-2">
        4.2 shared/jwt_manager.py - אימות JWT <span class="page-number-hebrew">עמוד 28</span>
        <div class="toc-entry toc-level-3">
            4.2.1 פונקציות יצירת טוקנים <span class="page-number-hebrew">עמוד 29</span>
        </div>
        <div class="toc-entry toc-level-3">
            4.2.2 אימות טוקנים ואבטחה <span class="page-number-hebrew">עמוד 30</span>
        </div>
    </div>
</div>

<div class="toc-entry toc-level-1">
    <strong>5. ניתוח מלא של שירות הצפייה</strong>
    <span class="page-number-hebrew">עמוד 32</span>
    <div class="toc-entry toc-level-2">
        5.1 watcher-service/watcher.py - השירות הראשי <span class="page-number-hebrew">עמוד 33</span>
        <div class="toc-entry toc-level-3">
            5.1.1 הצהרות ייבוא ותלויות <span class="page-number-hebrew">עמוד 34</span>
        </div>
        <div class="toc-entry toc-level-3">
            5.1.2 מחלקת FileProcessor - פירוק מלא <span class="page-number-hebrew">עמוד 35</span>
        </div>
        <div class="toc-entry toc-level-3">
            5.1.3 מחלקת WatcherEventHandler - אירועי קבצים <span class="page-number-hebrew">עמוד 38</span>
        </div>
        <div class="toc-entry toc-level-3">
            5.1.4 מחלקת WatcherService - הלוגיקה הראשית <span class="page-number-hebrew">עמוד 40</span>
        </div>
        <div class="toc-entry toc-level-3">
            5.1.5 פונקציה ראשית והפעלת השירות <span class="page-number-hebrew">עמוד 42</span>
        </div>
    </div>
    <div class="toc-entry toc-level-2">
        5.2 watcher-service/config_ui.py - ממשק הגדרות <span class="page-number-hebrew">עמוד 44</span>
    </div>
    <div class="toc-entry toc-level-2">
        5.3 watcher-service/config.yaml - קובץ הגדרות <span class="page-number-hebrew">עמוד 46</span>
    </div>
    <div class="toc-entry toc-level-2">
        5.4 watcher-service/templates/config_form.html - ממשק ווב <span class="page-number-hebrew">עמוד 48</span>
    </div>
</div>

<div class="toc-entry toc-level-1">
    <strong>6. ניתוח מלא של שירות הרישום</strong>
    <span class="page-number-hebrew">עמוד 50</span>
    <div class="toc-entry toc-level-2">
        6.1 logger-service/logger.py - השירות הראשי <span class="page-number-hebrew">עמוד 51</span>
        <div class="toc-entry toc-level-3">
            6.1.1 מודלי Pydantic - אימות נתונים <span class="page-number-hebrew">עמוד 52</span>
        </div>
        <div class="toc-entry toc-level-3">
            6.1.2 מחלקת LoggerService - הלוגיקה המרכזית <span class="page-number-hebrew">עמוד 54</span>
        </div>
        <div class="toc-entry toc-level-3">
            6.1.3 נקודות קצה FastAPI - מטפלי HTTP <span class="page-number-hebrew">עמוד 56</span>
        </div>
        <div class="toc-entry toc-level-3">
            6.1.4 יצירת קבצי רישום וניהול <span class="page-number-hebrew">עמוד 58</span>
        </div>
    </div>
    <div class="toc-entry toc-level-2">
        6.2 logger-service/config_ui.py - ממשק הגדרות <span class="page-number-hebrew">עמוד 60</span>
    </div>
    <div class="toc-entry toc-level-2">
        6.3 logger-service/config.yaml - קובץ הגדרות <span class="page-number-hebrew">עמוד 62</span>
    </div>
    <div class="toc-entry toc-level-2">
        6.4 logger-service/templates/config_form.html - ממשק ווב <span class="page-number-hebrew">עמוד 64</span>
    </div>
</div>

<div class="toc-entry toc-level-1">
    <strong>7. הגדרת Docker</strong>
    <span class="page-number-hebrew">עמוד 66</span>
    <div class="toc-entry toc-level-2">
        7.1 Dockerfile.watcher - מכולת הצפייה <span class="page-number-hebrew">עמוד 67</span>
    </div>
    <div class="toc-entry toc-level-2">
        7.2 Dockerfile.logger - מכולת הרישום <span class="page-number-hebrew">עמוד 68</span>
    </div>
    <div class="toc-entry toc-level-2">
        7.3 docker-compose.yml - תזמור <span class="page-number-hebrew">עמוד 69</span>
    </div>
</div>

<div class="toc-entry toc-level-1">
    <strong>8. בדיקות ואימות</strong>
    <span class="page-number-hebrew">עמוד 71</span>
    <div class="toc-entry toc-level-2">
        8.1 test_system.py - בדיקות אוטומטיות <span class="page-number-hebrew">עמוד 72</span>
    </div>
    <div class="toc-entry toc-level-2">
        8.2 validate_system.py - אימות מערכת <span class="page-number-hebrew">עמוד 74</span>
    </div>
    <div class="toc-entry toc-level-2">
        8.3 נהלי בדיקה ידניים <span class="page-number-hebrew">עמוד 76</span>
    </div>
</div>

<div class="toc-entry toc-level-1">
    <strong>9. ניהול הגדרות</strong>
    <span class="page-number-hebrew">עמוד 78</span>
    <div class="toc-entry toc-level-2">
        9.1 מבנה הגדרות YAML <span class="page-number-hebrew">עמוד 79</span>
    </div>
    <div class="toc-entry toc-level-2">
        9.2 משתני סביבה <span class="page-number-hebrew">עמוד 80</span>
    </div>
    <div class="toc-entry toc-level-2">
        9.3 ממשקי הגדרות מבוססי ווב <span class="page-number-hebrew">עמוד 81</span>
    </div>
</div>

<div class="toc-entry toc-level-1">
    <strong>10. אבטחה ואימות</strong>
    <span class="page-number-hebrew">עמוד 83</span>
    <div class="toc-entry toc-level-2">
        10.1 מחזור חיי טוקן JWT <span class="page-number-hebrew">עמוד 84</span>
    </div>
    <div class="toc-entry toc-level-2">
        10.2 אבטחת קבצים ואימות <span class="page-number-hebrew">עמוד 85</span>
    </div>
    <div class="toc-entry toc-level-2">
        10.3 אבטחת רשת <span class="page-number-hebrew">עמוד 86</span>
    </div>
</div>

<div class="toc-entry toc-level-1">
    <strong>11. ניטור ורישום</strong>
    <span class="page-number-hebrew">עמוד 88</span>
    <div class="toc-entry toc-level-2">
        11.1 ניתוח יומני שירות <span class="page-number-hebrew">עמוד 89</span>
    </div>
    <div class="toc-entry toc-level-2">
        11.2 נקודות קצה בדיקת בריאות <span class="page-number-hebrew">עמוד 90</span>
    </div>
    <div class="toc-entry toc-level-2">
        11.3 מערכות התראת שגיאות <span class="page-number-hebrew">עמוד 91</span>
    </div>
</div>

<div class="toc-entry toc-level-1">
    <strong>12. מדריך פתרון בעיות</strong>
    <span class="page-number-hebrew">עמוד 93</span>
    <div class="toc-entry toc-level-2">
        12.1 בעיות נפוצות ופתרונות <span class="page-number-hebrew">עמוד 94</span>
    </div>
    <div class="toc-entry toc-level-2">
        12.2 מצב דיבוג ורישום מתקדם <span class="page-number-hebrew">עמוד 96</span>
    </div>
    <div class="toc-entry toc-level-2">
        12.3 אופטימיזציה של ביצועים <span class="page-number-hebrew">עמוד 98</span>
    </div>
</div>

<div class="toc-entry toc-level-1">
    <strong>13. מرجع API</strong>
    <span class="page-number-hebrew">עמוד 100</span>
    <div class="toc-entry toc-level-2">
        13.1 API שירות הרישום <span class="page-number-hebrew">עמוד 101</span>
    </div>
    <div class="toc-entry toc-level-2">
        13.2 API הגדרות <span class="page-number-hebrew">עמוד 103</span>
    </div>
    <div class="toc-entry toc-level-2">
        13.3 קודי סטטוס HTTP וטיפול בשגיאות <span class="page-number-hebrew">עמוד 105</span>
    </div>
</div>

<div class="toc-entry toc-level-1">
    <strong>14. נספחים</strong>
    <span class="page-number-hebrew">עמוד 107</span>
    <div class="toc-entry toc-level-2">
        14.1 רשימות קוד מלאות <span class="page-number-hebrew">עמוד 108</span>
    </div>
    <div class="toc-entry toc-level-2">
        14.2 תבניות הגדרות <span class="page-number-hebrew">עמוד 115</span>
    </div>
    <div class="toc-entry toc-level-2">
        14.3 מילון מונחים טכניים <span class="page-number-hebrew">עמוד 120</span>
    </div>
</div>

</div>

</div>

</div>

---

**📋 Note:** This is the Table of Contents for the complete SASA Software Microservices System documentation. Each section will provide detailed, line-by-line analysis of every file, function, and configuration option in both English and Hebrew.

**הערה:** זהו תוכן העניינים למסמך המלא של מערכת המיקרו-שירותים של SASA Software. כל קטע יספק ניתוח מפורט, שורה אחר שורה, של כל קובץ, פונקציה ואפשרות הגדרה בעברית ובאנגלית.

---

<!-- SECTION 1: PROJECT OVERVIEW & INTRODUCTION -->
<div class="page-break">
<h1 style="text-align: center; border-bottom: 3px solid #e74c3c; padding-bottom: 20px; color: #2c3e50;">
    📊 SECTION 1: PROJECT OVERVIEW & INTRODUCTION<br>
    קטע 1: סקירת פרויקט ומבוא
</h1>

<div class="bilingual-container">

<!-- ENGLISH SECTION -->
<div class="english-section">
<h2>🎯 1.1 What is SASA Software Microservices System?</h2>

<p><strong>SASA Software Microservices System</strong> is a comprehensive, enterprise-grade file monitoring and logging solution built with modern microservices architecture. The system provides secure, real-time file processing with JWT-authenticated communication between services.</p>

<h3>🏗️ Core Components:</h3>
<ul>
    <li><strong>Watcher Service</strong> - Monitors directories for new files</li>
    <li><strong>Logger Service</strong> - Processes and logs file metadata</li>
    <li><strong>Configuration UIs</strong> - Web-based management interfaces</li>
    <li><strong>Shared Libraries</strong> - Common utilities and JWT management</li>
</ul>

<h3>🔐 Security Features:</h3>
<ul>
    <li><strong>JWT Authentication</strong> - Secure inter-service communication</li>
    <li><strong>File Validation</strong> - Size limits, type checking, sanitization</li>
    <li><strong>Network Security</strong> - Rate limiting, CORS protection</li>
    <li><strong>Error Handling</strong> - Comprehensive logging and notifications</li>
</ul>

<h3>📈 Key Benefits:</h3>
<ul>
    <li><strong>Scalable Architecture</strong> - Microservices design for easy scaling</li>
    <li><strong>Real-time Processing</strong> - Immediate file detection and processing</li>
    <li><strong>Complete Auditability</strong> - Full logging of all file operations</li>
    <li><strong>Easy Configuration</strong> - Web-based configuration management</li>
    <li><strong>Production Ready</strong> - Docker containerization and orchestration</li>
</ul>

<h2>🏛️ 1.2 System Architecture Deep Dive</h2>

<div style="background: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0;">
<pre style="font-family: 'Courier New', monospace; font-size: 12px; line-height: 1.4;">
┌─────────────────────────────────────────────────────────────────┐
│                    SASA SOFTWARE ARCHITECTURE                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐    JWT/HTTP     ┌─────────────────┐       │
│  │   Watcher       │◄───────────────►│   Logger        │       │
│  │   Service       │   Secure Auth   │   Service       │       │
│  │   (Port 8000)   │   HS256 Token   │   (Port 8001)   │       │
│  └─────────────────┘                 └─────────────────┘       │
│           │                                   │                 │
│           ▼                                   ▼                 │
│  ┌─────────────────┐                 ┌─────────────────┐       │
│  │   Config UI     │                 │   Config UI     │       │
│  │   (Port 8080)   │                 │   (Port 8081)   │       │
│  │   FastAPI Web   │                 │   FastAPI Web   │       │
│  └─────────────────┘                 └─────────────────┘       │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                 SHARED COMPONENTS                       │   │
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────────┐  │   │
│  │  │ JWT Manager │ │    Utils    │ │  Notifications  │  │   │
│  │  │   HS256     │ │   Logging   │ │  Email/Syslog   │  │   │
│  │  │ Validation  │ │ Config Mgmt │ │   Error Alerts  │  │   │
│  │  └─────────────┘ └─────────────┘ └─────────────────┘  │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                   FILE WORKFLOW                         │   │
│  │                                                         │   │
│  │  📁 watched/ ──► 🔍 Detection ──► 📊 Metadata ──►     │   │
│  │                                                         │   │
│  │  🔐 JWT Token ──► 📡 HTTP POST ──► 📄 Log Creation ──► │   │
│  │                                                         │   │
│  │  📁 processed/ ◄── 🚀 File Move ◄── ✅ Success        │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
</pre>
</div>

<h3>🔄 Request Flow Explanation:</h3>
<ol>
    <li><strong>File Detection</strong> - Watchdog monitors `./watched` directory</li>
    <li><strong>Metadata Extraction</strong> - File info: name, size, hash, timestamp</li>
    <li><strong>JWT Creation</strong> - Secure token with HS256 algorithm</li>
    <li><strong>HTTP Request</strong> - POST to Logger Service with authentication</li>
    <li><strong>Validation</strong> - JWT verification and data validation</li>
    <li><strong>Log Creation</strong> - Structured log file with timestamp</li>
    <li><strong>File Archival</strong> - Move to `./processed` directory</li>
    <li><strong>Response</strong> - Success/failure notification</li>
</ol>

<h2>🛠️ 1.3 Technology Stack</h2>

<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
    <thead style="background: #3498db; color: white;">
        <tr>
            <th style="padding: 12px; border: 1px solid #ddd;">Layer</th>
            <th style="padding: 12px; border: 1px solid #ddd;">Technology</th>
            <th style="padding: 12px; border: 1px solid #ddd;">Purpose</th>
            <th style="padding: 12px; border: 1px solid #ddd;">Version</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>Runtime</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Python</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Main programming language</td>
            <td style="padding: 8px; border: 1px solid #ddd;">3.8+</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>Web Framework</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">FastAPI</td>
            <td style="padding: 8px; border: 1px solid #ddd;">REST API and web interfaces</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Latest</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>ASGI Server</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Uvicorn</td>
            <td style="padding: 8px; border: 1px solid #ddd;">High-performance async server</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Latest</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>File Monitoring</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Watchdog</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Cross-platform file system events</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Latest</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>Authentication</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">PyJWT</td>
            <td style="padding: 8px; border: 1px solid #ddd;">JWT token creation and validation</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Latest</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>Data Validation</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Pydantic</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Request/response validation</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Latest</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>HTTP Client</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Requests</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Inter-service communication</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Latest</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>Templates</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Jinja2</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Web UI template rendering</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Latest</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>Configuration</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">PyYAML</td>
            <td style="padding: 8px; border: 1px solid #ddd;">YAML configuration files</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Latest</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>Containerization</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Docker</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Application containerization</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Latest</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>Orchestration</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Docker Compose</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Multi-container deployment</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Latest</td>
        </tr>
    </tbody>
</table>

<h2>🔒 1.4 Security Architecture</h2>

<h3>🛡️ JWT Authentication Flow:</h3>
<div style="background: #fff3cd; padding: 15px; border-radius: 5px; border-left: 5px solid #ffc107;">
<ol>
    <li><strong>Token Generation</strong>
        <ul>
            <li>Algorithm: HS256 (HMAC with SHA-256)</li>
            <li>Secret Key: Configurable shared secret</li>
            <li>Claims: Issuer, expiration time, file metadata</li>
            <li>Expiry: 5 minutes (configurable)</li>
        </ul>
    </li>
    <li><strong>Token Transmission</strong>
        <ul>
            <li>Header: Authorization: Bearer &lt;token&gt;</li>
            <li>Transport: HTTPS recommended for production</li>
            <li>Content-Type: application/json</li>
        </ul>
    </li>
    <li><strong>Token Validation</strong>
        <ul>
            <li>Signature verification with shared secret</li>
            <li>Expiration time validation</li>
            <li>Issuer verification</li>
            <li>Claims validation</li>
        </ul>
    </li>
</ol>
</div>

<h3>🔐 File Security Measures:</h3>
<ul>
    <li><strong>Filename Sanitization</strong> - Remove dangerous characters</li>
    <li><strong>Path Validation</strong> - Prevent directory traversal attacks</li>
    <li><strong>Size Limits</strong> - Configurable maximum file sizes</li>
    <li><strong>Type Filtering</strong> - Allow/deny specific file extensions</li>
    <li><strong>Content Validation</strong> - Optional content inspection</li>
</ul>

</div>

<!-- HEBREW SECTION -->
<div class="hebrew-section">
<h2>🎯 1.1 מה היא מערכת המיקרו-שירותים של SASA Software?</h2>

<p><strong>מערכת המיקרו-שירותים של SASA Software</strong> היא פתרון מקיף ברמה ארגונית לניטור קבצים ורישום, הבנוי עם ארכיטקטורת מיקרו-שירותים מודרנית. המערכת מספקת עיבוד קבצים מאובטח בזמן אמת עם תקשורת מאומתת JWT בין השירותים.</p>

<h3>🏗️ רכיבים מרכזיים:</h3>
<ul>
    <li><strong>שירות הצפייה</strong> - מנטר תיקיות עבור קבצים חדשים</li>
    <li><strong>שירות הרישום</strong> - מעבד ורושם מטא-נתונים של קבצים</li>
    <li><strong>ממשקי הגדרות</strong> - ממשקי ניהול מבוססי ווב</li>
    <li><strong>ספריות משותפות</strong> - כלי עזר נפוצים וניהול JWT</li>
</ul>

<h3>🔐 תכונות אבטחה:</h3>
<ul>
    <li><strong>אימות JWT</strong> - תקשורת מאובטחת בין שירותים</li>
    <li><strong>אימות קבצים</strong> - מגבלות גודל, בדיקת סוג, עיקור</li>
    <li><strong>אבטחת רשת</strong> - הגבלת קצב, הגנת CORS</li>
    <li><strong>טיפול בשגיאות</strong> - רישום מקיף והתראות</li>
</ul>

<h3>📈 יתרונות מרכזיים:</h3>
<ul>
    <li><strong>ארכיטקטורה מדרגית</strong> - עיצוב מיקרו-שירותים להרחבה קלה</li>
    <li><strong>עיבוד בזמן אמת</strong> - זיהוי ועיבוד מידי של קבצים</li>
    <li><strong>ביקורת מלאה</strong> - רישום מלא של כל פעולות הקבצים</li>
    <li><strong>הגדרה קלה</strong> - ניהול הגדרות מבוסס ווב</li>
    <li><strong>מוכן לייצור</strong> - קונטיינריזציה ותזמור Docker</li>
</ul>

<h2>🏛️ 1.2 צלילה עמוקה לארכיטקטורת המערכת</h2>

<div style="background: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0;">
<pre style="font-family: 'Courier New', monospace; font-size: 12px; line-height: 1.4;">
┌─────────────────────────────────────────────────────────────────┐
│                  ארכיטקטורת SASA SOFTWARE                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐    JWT/HTTP     ┌─────────────────┐       │
│  │     שירות       │◄───────────────►│     שירות       │       │
│  │     הצפייה      │   אימות מאובטח  │     הרישום      │       │
│  │   (פורט 8000)   │   טוקן HS256    │   (פורט 8001)   │       │
│  └─────────────────┘                 └─────────────────┘       │
│           │                                   │                 │
│           ▼                                   ▼                 │
│  ┌─────────────────┐                 ┌─────────────────┐       │
│  │   ממשק הגדרות   │                 │   ממשק הגדרות   │       │
│  │   (פורט 8080)   │                 │   (פורט 8081)   │       │
│  │   FastAPI ווב   │                 │   FastAPI ווב   │       │
│  └─────────────────┘                 └─────────────────┘       │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                 רכיבים משותפים                          │   │
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────────┐  │   │
│  │  │  מנהל JWT   │ │   כלי עזר   │ │    התראות       │  │   │
│  │  │   HS256     │ │    רישום    │ │  אימייל/Syslog  │  │   │
│  │  │   אימות     │ │  ניהול הגדרות│ │  התראות שגיאה   │  │   │
│  │  └─────────────┘ └─────────────┘ └─────────────────┘  │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                   זרימת קבצים                           │   │
│  │                                                         │   │
│  │  📁 watched/ ──► 🔍 זיהוי ──► 📊 מטא-נתונים ──►       │   │
│  │                                                         │   │
│  │  🔐 טוקן JWT ──► 📡 HTTP POST ──► 📄 יצירת לוג ──►     │   │
│  │                                                         │   │
│  │  📁 processed/ ◄── 🚀 העברת קובץ ◄── ✅ הצלחה         │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
</pre>
</div>

<h3>🔄 הסבר זרימת הבקשות:</h3>
<ol>
    <li><strong>זיהוי קבצים</strong> - Watchdog מנטר את תיקיית `./watched`</li>
    <li><strong>חילוץ מטא-נתונים</strong> - מידע קובץ: שם, גודל, hash, חותמת זמן</li>
    <li><strong>יצירת JWT</strong> - טוקן מאובטח עם אלגוריתם HS256</li>
    <li><strong>בקשת HTTP</strong> - POST לשירות הרישום עם אימות</li>
    <li><strong>אימות</strong> - אימות JWT ואימות נתונים</li>
    <li><strong>יצירת לוג</strong> - קובץ לוג מובנה עם חותמת זמן</li>
    <li><strong>ארכיון קבצים</strong> - העברה לתיקיית `./processed`</li>
    <li><strong>תגובה</strong> - התראת הצלחה/כישלון</li>
</ol>

<h2>🛠️ 1.3 מחסנית טכנולוגיות</h2>

<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
    <thead style="background: #3498db; color: white;">
        <tr>
            <th style="padding: 12px; border: 1px solid #ddd;">שכבה</th>
            <th style="padding: 12px; border: 1px solid #ddd;">טכנולוגיה</th>
            <th style="padding: 12px; border: 1px solid #ddd;">מטרה</th>
            <th style="padding: 12px; border: 1px solid #ddd;">גרסה</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>סביבת ריצה</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Python</td>
            <td style="padding: 8px; border: 1px solid #ddd;">שפת תכנות ראשית</td>
            <td style="padding: 8px; border: 1px solid #ddd;">3.8+</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>מסגרת ווב</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">FastAPI</td>
            <td style="padding: 8px; border: 1px solid #ddd;">REST API וממשקי ווב</td>
            <td style="padding: 8px; border: 1px solid #ddd;">אחרונה</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>שרת ASGI</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Uvicorn</td>
            <td style="padding: 8px; border: 1px solid #ddd;">שרת אסינכרוני בעל ביצועים גבוהים</td>
            <td style="padding: 8px; border: 1px solid #ddd;">אחרונה</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>ניטור קבצים</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Watchdog</td>
            <td style="padding: 8px; border: 1px solid #ddd;">אירועי מערכת קבצים חוצי פלטפורמות</td>
            <td style="padding: 8px; border: 1px solid #ddd;">אחרונה</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>אימות</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">PyJWT</td>
            <td style="padding: 8px; border: 1px solid #ddd;">יצירה ואימות של טוקני JWT</td>
            <td style="padding: 8px; border: 1px solid #ddd;">אחרונה</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>אימות נתונים</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Pydantic</td>
            <td style="padding: 8px; border: 1px solid #ddd;">אימות בקשות/תגובות</td>
            <td style="padding: 8px; border: 1px solid #ddd;">אחרונה</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>לקוח HTTP</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Requests</td>
            <td style="padding: 8px; border: 1px solid #ddd;">תקשורת בין-שירותית</td>
            <td style="padding: 8px; border: 1px solid #ddd;">אחרונה</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>תבניות</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Jinja2</td>
            <td style="padding: 8px; border: 1px solid #ddd;">עיבוד תבניות ממשק ווב</td>
            <td style="padding: 8px; border: 1px solid #ddd;">אחרונה</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>הגדרות</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">PyYAML</td>
            <td style="padding: 8px; border: 1px solid #ddd;">קבצי הגדרות YAML</td>
            <td style="padding: 8px; border: 1px solid #ddd;">אחרונה</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>קונטיינריזציה</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Docker</td>
            <td style="padding: 8px; border: 1px solid #ddd;">קונטיינריזציה של אפליקציות</td>
            <td style="padding: 8px; border: 1px solid #ddd;">אחרונה</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>תזמור</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Docker Compose</td>
            <td style="padding: 8px; border: 1px solid #ddd;">פריסה רב-קונטיינרית</td>
            <td style="padding: 8px; border: 1px solid #ddd;">אחרונה</td>
        </tr>
    </tbody>
</table>

<h2>🔒 1.4 ארכיטקטורת אבטחה</h2>

<h3>🛡️ זרימת אימות JWT:</h3>
<div style="background: #fff3cd; padding: 15px; border-radius: 5px; border-right: 5px solid #ffc107;">
<ol>
    <li><strong>יצירת טוקן</strong>
        <ul>
            <li>אלגוריתם: HS256 (HMAC עם SHA-256)</li>
            <li>מפתח סודי: סוד משותף הניתן להגדרה</li>
            <li>טענות: מנפיק, זמן תפוגה, מטא-נתוני קובץ</li>
            <li>תפוגה: 5 דקות (ניתן להגדרה)</li>
        </ul>
    </li>
    <li><strong>העברת טוכן</strong>
        <ul>
            <li>כותרת: Authorization: Bearer &lt;token&gt;</li>
            <li>תחבורה: HTTPS מומלץ לייצור</li>
            <li>Content-Type: application/json</li>
        </ul>
    </li>
    <li><strong>אימות טוקן</strong>
        <ul>
            <li>אימות חתימה עם סוד משותף</li>
            <li>אימות זמן תפוגה</li>
            <li>אימות מנפיק</li>
            <li>אימות טענות</li>
        </ul>
    </li>
</ol>
</div>

<h3>🔐 אמצעי אבטחת קבצים:</h3>
<ul>
    <li><strong>עיקור שמות קבצים</strong> - הסרת תווים מסוכנים</li>
    <li><strong>אימות נתיב</strong> - מניעת התקפות חציית תיקיות</li>
    <li><strong>מגבלות גודל</strong> - גדלי קבצים מקסימליים הניתנים להגדרה</li>
    <li><strong>סינון סוגים</strong> - אפשר/מנע סיומות קבצים ספציפיות</li>
    <li><strong>אימות תוכן</strong> - בדיקת תוכן אופציונלית</li>
</ul>

</div>

</div>

</div>

---

<!-- SECTION 2: QUICK START GUIDE -->
<div class="page-break">
<h1 style="text-align: center; border-bottom: 3px solid #28a745; padding-bottom: 20px; color: #2c3e50;">
    🚀 SECTION 2: QUICK START GUIDE<br>
    קטע 2: מדריך התחלה מהירה
</h1>

<div class="bilingual-container">

<!-- ENGLISH SECTION -->
<div class="english-section">
<h2>⚡ 2.1 Prerequisites & Installation</h2>

<h3>📋 System Requirements</h3>
<div style="background: #e8f4fd; padding: 15px; border-radius: 5px; border-left: 5px solid #0066cc;">
<h4>💻 Hardware Requirements:</h4>
<ul>
    <li><strong>RAM:</strong> Minimum 4GB, Recommended 8GB+</li>
    <li><strong>Storage:</strong> 2GB free space for system + logs</li>
    <li><strong>CPU:</strong> Any modern processor (x64 recommended)</li>
    <li><strong>Network:</strong> Internet connection for dependencies</li>
</ul>

<h4>🖥️ Operating System Support:</h4>
<ul>
    <li><strong>Windows:</strong> Windows 10/11 (Primary support)</li>
    <li><strong>Linux:</strong> Ubuntu 18.04+, CentOS 7+, Debian 9+</li>
    <li><strong>macOS:</strong> macOS 10.15+ (Catalina or later)</li>
</ul>
</div>

<h3>🛠️ Required Software Installation</h3>

<h4>Step 1: Install Python 3.8+</h4>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
<strong>Windows:</strong><br>
1. Download from <a href="https://python.org/downloads/">python.org/downloads</a><br>
2. Run installer as Administrator<br>
3. ✅ Check "Add Python to PATH"<br>
4. ✅ Check "Install pip"<br>
5. Verify: <code>python --version</code><br><br>

<strong>Linux (Ubuntu/Debian):</strong><br>
<code>sudo apt update</code><br>
<code>sudo apt install python3 python3-pip python3-venv</code><br><br>

<strong>macOS:</strong><br>
<code>brew install python3</code><br>

# Or download from python.org

</div>

<h4>Step 2: Install Git (Optional but Recommended)</h4>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
<strong>Windows:</strong> Download from <a href="https://git-scm.com">git-scm.com</a><br>
<strong>Linux:</strong> <code>sudo apt install git</code><br>
<strong>macOS:</strong> <code>brew install git</code><br>
<strong>Verify:</strong> <code>git --version</code>
</div>

<h4>Step 3: Install Docker (For Container Deployment)</h4>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
<strong>Windows:</strong> Download Docker Desktop from <a href="https://docker.com">docker.com</a><br>
<strong>Linux:</strong> <code>curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh</code><br>
<strong>macOS:</strong> Download Docker Desktop from <a href="https://docker.com">docker.com</a><br>
<strong>Verify:</strong> <code>docker --version && docker-compose --version</code>
</div>

<h2>🎯 2.2 Project Setup</h2>

<h3>Method 1: Download & Extract (Recommended)</h3>
<div style="background: #d4edda; padding: 15px; border-radius: 5px; border-left: 5px solid #28a745;">
<ol>
    <li><strong>Navigate to your project location:</strong>
        <pre>cd "C:\Users\haspe\OneDrive\Desktop\מהמחשב הישן\VScode\sasa_Software"</pre>
    </li>
    <li><strong>Verify project structure:</strong>
        <pre>dir  # Windows
ls -la  # Linux/Mac</pre>
        You should see:
        <ul>
            <li>📁 shared/</li>
            <li>📁 watcher-service/</li>
            <li>📁 logger-service/</li>
            <li>📄 docker-compose.yml</li>
            <li>📄 requirements.txt</li>
            <li>📄 start.bat (Windows)</li>
        </ul>
    </li>
</ol>
</div>

<h3>Method 2: Git Clone (If Available)</h3>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
git clone https://github.com/haspeltamir/sasa_Software.git<br>
cd sasa_Software
</div>

<h2>🐳 2.3 Docker Deployment Method (Recommended)</h2>

<div style="background: #cce5ff; padding: 20px; border-radius: 8px; border-left: 5px solid #0066cc;">
<h3>✨ Advantages of Docker Method:</h3>
<ul>
    <li>✅ No Python environment setup needed</li>
    <li>✅ Consistent environment across all systems</li>
    <li>✅ Easy scaling and management</li>
    <li>✅ Automatic dependency management</li>
    <li>✅ Production-ready deployment</li>
</ul>
</div>

<h3>Step 1: Verify Docker Installation</h3>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
# Check Docker is running<br>
docker --version<br>
docker-compose --version<br><br>

# Expected output:<br>

# Docker version 20.10.x+<br>

# Docker Compose version 2.x.x+

</div>

<h3>Step 2: Start All Services with Docker</h3>

<h4>🪟 Windows PowerShell:</h4>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
# Navigate to project directory<br>
cd "C:\Users\haspe\OneDrive\Desktop\מהמחשב הישן\VScode\sasa_Software"<br><br>

# Method A: Use startup script (Easiest)<br>

.\start.bat<br><br>

# Method B: Direct Docker Compose<br>

docker-compose up -d --build<br><br>

# Method C: PowerShell script<br>

.\start.ps1

</div>

<h4>🐧 Linux/Mac Terminal:</h4>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
# Navigate to project directory<br>
cd /path/to/sasa_Software<br><br>

# Make script executable<br>

chmod +x start.sh<br><br>

# Start services<br>

./start.sh<br><br>

# Or direct Docker Compose<br>

docker-compose up -d --build

</div>

<h3>Step 3: Verify Services are Running</h3>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
# Check container status<br>
docker-compose ps<br><br>

# Expected output:<br>

# Name State Ports<br>

# sasa-logger-service Up 0.0.0.0:8001->8001/tcp<br>

# sasa-watcher-service Up <br>

# sasa-logger-config Up 0.0.0.0:8081->8081/tcp<br>

# sasa-watcher-config Up 0.0.0.0:8082->8082/tcp<br><br>

# View logs<br>

docker-compose logs -f

</div>

<h2>🐍 2.4 Python Direct Execution Method</h2>

<div style="background: #fff3cd; padding: 20px; border-radius: 8px; border-left: 5px solid #ffc107;">
<h3>⚠️ When to Use Direct Python:</h3>
<ul>
    <li>🔧 Development and debugging</li>
    <li>🎯 Custom configuration testing</li>
    <li>🔍 Detailed logging and monitoring</li>
    <li>⚡ Quick testing without containers</li>
</ul>
</div>

<h3>Step 1: Create Virtual Environment</h3>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
# Windows<br>
python -m venv sasa_env<br>
sasa_env\Scripts\activate<br><br>

# Linux/Mac<br>

python3 -m venv sasa_env<br>
source sasa_env/bin/activate<br><br>

# Verify activation (should show (sasa_env))<br>

# (sasa_env) C:\...\sasa_Software>

</div>

<h3>Step 2: Install Dependencies</h3>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
# Upgrade pip first<br>
python -m pip install --upgrade pip<br><br>

# Install all requirements<br>

pip install -r requirements.txt<br><br>

# Verify installation<br>

pip list<br><br>

# Expected packages:<br>

# fastapi==0.x.x<br>

# uvicorn==0.x.x<br>

# watchdog==x.x.x<br>

# pyjwt==x.x.x<br>

# requests==x.x.x<br>

# pydantic==x.x.x<br>

# jinja2==x.x.x<br>

# pyyaml==x.x.x

</div>

<h3>Step 3: Start Services in Multiple Terminals</h3>

<div style="background: #e8f4fd; padding: 15px; border-radius: 5px; border-left: 5px solid #0066cc;">
<h4>🔥 Important: You need 4 separate terminal windows!</h4>
<p>Each service runs in its own terminal for better monitoring and control.</p>
</div>

<h4>Terminal 1: Logger Service</h4>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
# Windows<br>
cd "C:\Users\haspe\OneDrive\Desktop\מהמחשב הישן\VScode\sasa_Software"<br>
sasa_env\Scripts\activate<br>
python logger-service/logger.py<br><br>

# Linux/Mac<br>

cd /path/to/sasa_Software<br>
source sasa_env/bin/activate<br>
python logger-service/logger.py<br><br>

# Expected output:<br>

# INFO: Started server process [12345]<br>

# INFO: Uvicorn running on http://0.0.0.0:8001

</div>

<h4>Terminal 2: Watcher Service (Wait for Logger to start first)</h4>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
# Wait 10 seconds after Logger starts, then:<br><br>

# Windows<br>

cd "C:\Users\haspe\OneDrive\Desktop\מהמחשב הישן\VScode\sasa_Software"<br>
sasa_env\Scripts\activate<br>
python watcher-service/watcher.py<br><br>

# Linux/Mac<br>

cd /path/to/sasa_Software<br>
source sasa_env/bin/activate<br>
python watcher-service/watcher.py<br><br>

# Expected output:<br>

# INFO: Watcher Service started successfully<br>

# INFO: Starting to watch directory: ./watched

</div>

<h4>Terminal 3: Logger Configuration UI (Optional)</h4>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
# Windows<br>
cd "C:\Users\haspe\OneDrive\Desktop\מהמחשב הישן\VScode\sasa_Software"<br>
sasa_env\Scripts\activate<br>
python logger-service/config_ui.py<br><br>

# Expected output:<br>

# INFO: Uvicorn running on http://0.0.0.0:8081

</div>

<h4>Terminal 4: Watcher Configuration UI (Optional)</h4>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
# Windows<br>
cd "C:\Users\haspe\OneDrive\Desktop\מהמחשב הישן\VScode\sasa_Software"<br>
sasa_env\Scripts\activate<br>
python watcher-service/config_ui.py<br><br>

# Expected output:<br>

# INFO: Uvicorn running on http://0.0.0.0:8082

</div>

<h2>🧪 2.5 First System Test & Verification</h2>

<h3>Step 1: Verify All Services are Running</h3>
<div style="background: #d4edda; padding: 15px; border-radius: 5px; border-left: 5px solid #28a745;">
<h4>📊 Service Status Check:</h4>
<table style="width: 100%; border-collapse: collapse; margin: 10px 0;">
    <thead style="background: #28a745; color: white;">
        <tr>
            <th style="padding: 8px; border: 1px solid #ddd;">Service</th>
            <th style="padding: 8px; border: 1px solid #ddd;">URL</th>
            <th style="padding: 8px; border: 1px solid #ddd;">Status Check</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;">Logger Service</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><a href="http://localhost:8001">http://localhost:8001</a></td>
            <td style="padding: 8px; border: 1px solid #ddd;">✅ Should show FastAPI docs</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;">Health Check</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><a href="http://localhost:8001/health">http://localhost:8001/health</a></td>
            <td style="padding: 8px; border: 1px solid #ddd;">✅ Should show JSON status</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;">Logger Config UI</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><a href="http://localhost:8081">http://localhost:8081</a></td>
            <td style="padding: 8px; border: 1px solid #ddd;">✅ Should show config form</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;">Watcher Config UI</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><a href="http://localhost:8082">http://localhost:8082</a></td>
            <td style="padding: 8px; border: 1px solid #ddd;">✅ Should show config form</td>
        </tr>
    </tbody>
</table>
</div>

<h3>Step 2: Create Your First Test File</h3>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
# Windows PowerShell<br>
echo "Hello SASA Software! This is my first test file." > watched\my_first_test.txt<br><br>

# Linux/Mac<br>

echo "Hello SASA Software! This is my first test file." > watched/my_first_test.txt<br><br>

# Alternative: Create with any text editor<br>

# Just save any file to the 'watched' directory

</div>

<h3>Step 3: Watch the Magic Happen! 🎭</h3>
<div style="background: #e8f4fd; padding: 20px; border-radius: 8px; border-left: 5px solid #0066cc;">
<h4>🔍 What You Should See:</h4>
<ol>
    <li><strong>Watcher Service Terminal:</strong>
        <pre>INFO: Added my_first_test.txt to processing queue
INFO: Processing file: ./watched/my_first_test.txt
INFO: Successfully sent metadata for my_first_test.txt
INFO: Moved my_first_test.txt to processed directory</pre>
    </li>
    <li><strong>Logger Service Terminal:</strong>
        <pre>INFO: Incoming request: POST /log
INFO: Processing log request for file: my_first_test.txt
INFO: Successfully created log file: logs\my_first_test-20251003T123456Z.txt
INFO: Request completed: 200 in 0.005s</pre>
    </li>
</ol>
</div>

<h3>Step 4: Verify Results</h3>
<div style="background: #d4edda; padding: 15px; border-radius: 5px; border-left: 5px solid #28a745;">
<h4>📁 Check These Locations:</h4>
<ol>
    <li><strong>processed/ directory:</strong> Your original file should be here</li>
    <li><strong>logs/ directory:</strong> New log file with timestamp should be created</li>
</ol>

<h4>📄 Sample Log File Content:</h4>
<pre>Filename: my_first_test.txt
Size: 52B
Created At: 2025-10-03T12:34:56Z
Hash: a1b2c3d4e5f6789012345678901234567890abcd1234567890abcd1234567890
Processed At: 2025-10-03T12:34:58Z</pre>
</div>

<h3>Step 5: Test Configuration UIs</h3>
<div style="background: #fff3cd; padding: 15px; border-radius: 5px; border-left: 5px solid #ffc107;">
<ol>
    <li><strong>Open Logger Config UI:</strong> <a href="http://localhost:8081">http://localhost:8081</a>
        <ul>
            <li>✅ Try changing log directory</li>
            <li>✅ Modify log file template</li>
            <li>✅ Test email notification settings</li>
        </ul>
    </li>
    <li><strong>Open Watcher Config UI:</strong> <a href="http://localhost:8082">http://localhost:8082</a>
        <ul>
            <li>✅ Change watch directory</li>
            <li>✅ Modify file patterns</li>
            <li>✅ Test retry settings</li>
        </ul>
    </li>
</ol>
</div>

</div>

<!-- HEBREW SECTION -->
<div class="hebrew-section">
<h2>⚡ 2.1 דרישות מוקדמות והתקנה</h2>

<h3>📋 דרישות מערכת</h3>
<div style="background: #e8f4fd; padding: 15px; border-radius: 5px; border-right: 5px solid #0066cc;">
<h4>💻 דרישות חומרה:</h4>
<ul>
    <li><strong>זיכרון:</strong> מינימום 4GB, מומלץ 8GB+</li>
    <li><strong>אחסון:</strong> 2GB מקום פנוי למערכת + יומנים</li>
    <li><strong>מעבד:</strong> כל מעבד מודרני (x64 מומלץ)</li>
    <li><strong>רשת:</strong> חיבור אינטרנט לתלויות</li>
</ul>

<h4>🖥️ תמיכה במערכות הפעלה:</h4>
<ul>
    <li><strong>Windows:</strong> Windows 10/11 (תמיכה ראשית)</li>
    <li><strong>Linux:</strong> Ubuntu 18.04+, CentOS 7+, Debian 9+</li>
    <li><strong>macOS:</strong> macOS 10.15+ (Catalina או חדש יותר)</li>
</ul>
</div>

<h3>🛠️ התקנת תוכנה נדרשת</h3>

<h4>שלב 1: התקנת Python 3.8+</h4>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
<strong>Windows:</strong><br>
1. הורד מ-<a href="https://python.org/downloads/">python.org/downloads</a><br>
2. הרץ את המתקין כמנהל<br>
3. ✅ סמן "Add Python to PATH"<br>
4. ✅ סמן "Install pip"<br>
5. וודא: <code>python --version</code><br><br>

<strong>Linux (Ubuntu/Debian):</strong><br>
<code>sudo apt update</code><br>
<code>sudo apt install python3 python3-pip python3-venv</code><br><br>

<strong>macOS:</strong><br>
<code>brew install python3</code><br>

# או הורד מ-python.org

</div>

<h4>שלב 2: התקנת Git (אופציונלי אבל מומלץ)</h4>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
<strong>Windows:</strong> הורד מ-<a href="https://git-scm.com">git-scm.com</a><br>
<strong>Linux:</strong> <code>sudo apt install git</code><br>
<strong>macOS:</strong> <code>brew install git</code><br>
<strong>וודא:</strong> <code>git --version</code>
</div>

<h4>שלב 3: התקנת Docker (לפריסה במכולות)</h4>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
<strong>Windows:</strong> הורד Docker Desktop מ-<a href="https://docker.com">docker.com</a><br>
<strong>Linux:</strong> <code>curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh</code><br>
<strong>macOS:</strong> הורד Docker Desktop מ-<a href="https://docker.com">docker.com</a><br>
<strong>וודא:</strong> <code>docker --version && docker-compose --version</code>
</div>

<h2>🎯 2.2 הגדרת פרויקט</h2>

<h3>שיטה 1: הורדה וחילוץ (מומלץ)</h3>
<div style="background: #d4edda; padding: 15px; border-radius: 5px; border-right: 5px solid #28a745;">
<ol>
    <li><strong>נווט למיקום הפרויקט שלך:</strong>
        <pre>cd "C:\Users\haspe\OneDrive\Desktop\מהמחשב הישן\VScode\sasa_Software"</pre>
    </li>
    <li><strong>וודא מבנה פרויקט:</strong>
        <pre>dir  # Windows
ls -la  # Linux/Mac</pre>
        אתה צריך לראות:
        <ul>
            <li>📁 shared/</li>
            <li>📁 watcher-service/</li>
            <li>📁 logger-service/</li>
            <li>📄 docker-compose.yml</li>
            <li>📄 requirements.txt</li>
            <li>📄 start.bat (Windows)</li>
        </ul>
    </li>
</ol>
</div>

<h3>שיטה 2: Git Clone (אם זמין)</h3>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
git clone https://github.com/haspeltamir/sasa_Software.git<br>
cd sasa_Software
</div>

<h2>🐳 2.3 שיטת פריסה עם Docker (מומלץ)</h2>

<div style="background: #cce5ff; padding: 20px; border-radius: 8px; border-right: 5px solid #0066cc;">
<h3>✨ יתרונות שיטת Docker:</h3>
<ul>
    <li>✅ אין צורך בהגדרת סביבת Python</li>
    <li>✅ סביבה עקבית בכל המערכות</li>
    <li>✅ הרחבה וניהול קלים</li>
    <li>✅ ניהול תלויות אוטומטי</li>
    <li>✅ פריסה מוכנה לייצור</li>
</ul>
</div>

<h3>שלב 1: וודא התקנת Docker</h3>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
# בדוק שDocker רץ<br>
docker --version<br>
docker-compose --version<br><br>

# פלט צפוי:<br>

# Docker version 20.10.x+<br>

# Docker Compose version 2.x.x+

</div>

<h3>שלב 2: הפעל את כל השירותים עם Docker</h3>

<h4>🪟 Windows PowerShell:</h4>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
# נווט לתיקיית הפרויקט<br>
cd "C:\Users\haspe\OneDrive\Desktop\מהמחשב הישן\VScode\sasa_Software"<br><br>

# שיטה A: השתמש בסקריפט הפעלה (הכי קל)<br>

.\start.bat<br><br>

# שיטה B: Docker Compose ישיר<br>

docker-compose up -d --build<br><br>

# שיטה C: סקריפט PowerShell<br>

.\start.ps1

</div>

<h4>🐧 Linux/Mac Terminal:</h4>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
# נווט לתיקיית הפרויקט<br>
cd /path/to/sasa_Software<br><br>

# הפוך את הסקריפט לבר הפעלה<br>

chmod +x start.sh<br><br>

# הפעל שירותים<br>

./start.sh<br><br>

# או Docker Compose ישיר<br>

docker-compose up -d --build

</div>

<h3>שלב 3: וודא שהשירותים פועלים</h3>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
# בדוק סטטוס מכולות<br>
docker-compose ps<br><br>

# פלט צפוי:<br>

# Name State Ports<br>

# sasa-logger-service Up 0.0.0.0:8001->8001/tcp<br>

# sasa-watcher-service Up <br>

# sasa-logger-config Up 0.0.0.0:8081->8081/tcp<br>

# sasa-watcher-config Up 0.0.0.0:8082->8082/tcp<br><br>

# צפה ביומנים<br>

docker-compose logs -f

</div>

<h2>🐍 2.4 שיטת הרצה ישירה עם Python</h2>

<div style="background: #fff3cd; padding: 20px; border-radius: 8px; border-right: 5px solid #ffc107;">
<h3>⚠️ מתי להשתמש ב-Python ישיר:</h3>
<ul>
    <li>🔧 פיתוח ודיבוג</li>
    <li>🎯 בדיקת הגדרות מותאמות</li>
    <li>🔍 רישום מפורט וניטור</li>
    <li>⚡ בדיקה מהירה ללא מכולות</li>
</ul>
</div>

<h3>שלב 1: צור סביבה וירטואלית</h3>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
# Windows<br>
python -m venv sasa_env<br>
sasa_env\Scripts\activate<br><br>

# Linux/Mac<br>

python3 -m venv sasa_env<br>
source sasa_env/bin/activate<br><br>

# וודא הפעלה (צריך להציג (sasa_env))<br>

# (sasa_env) C:\...\sasa_Software>

</div>

<h3>שלב 2: התקן תלויות</h3>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
# שדרג pip תחילה<br>
python -m pip install --upgrade pip<br><br>

# התקן את כל הדרישות<br>

pip install -r requirements.txt<br><br>

# וודא התקנה<br>

pip list<br><br>

# חבילות צפויות:<br>

# fastapi==0.x.x<br>

# uvicorn==0.x.x<br>

# watchdog==x.x.x<br>

# pyjwt==x.x.x<br>

# requests==x.x.x<br>

# pydantic==x.x.x<br>

# jinja2==x.x.x<br>

# pyyaml==x.x.x

</div>

<h3>שלב 3: הפעל שירותים במספר טרמינלים</h3>

<div style="background: #e8f4fd; padding: 15px; border-radius: 5px; border-right: 5px solid #0066cc;">
<h4>🔥 חשוב: אתה צריך 4 חלונות טרמינל נפרדים!</h4>
<p>כל שירות רץ בטרמינל משלו לניטור ובקרה טובים יותר.</p>
</div>

<h4>טרמינל 1: שירות הרישום</h4>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
# Windows<br>
cd "C:\Users\haspe\OneDrive\Desktop\מהמחשב הישן\VScode\sasa_Software"<br>
sasa_env\Scripts\activate<br>
python logger-service/logger.py<br><br>

# Linux/Mac<br>

cd /path/to/sasa_Software<br>
source sasa_env/bin/activate<br>
python logger-service/logger.py<br><br>

# פלט צפוי:<br>

# INFO: Started server process [12345]<br>

# INFO: Uvicorn running on http://0.0.0.0:8001

</div>

<h4>טרמינל 2: שירות הצפייה (המתן עד שהLogger יתחיל תחילה)</h4>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
# המתן 10 שניות אחרי שהLogger מתחיל, ואז:<br><br>

# Windows<br>

cd "C:\Users\haspe\OneDrive\Desktop\מהמחשב הישן\VScode\sasa_Software"<br>
sasa_env\Scripts\activate<br>
python watcher-service/watcher.py<br><br>

# Linux/Mac<br>

cd /path/to/sasa_Software<br>
source sasa_env/bin/activate<br>
python watcher-service/watcher.py<br><br>

# פלט צפוי:<br>

# INFO: Watcher Service started successfully<br>

# INFO: Starting to watch directory: ./watched

</div>

<h4>טרמינל 3: ממשק הגדרות Logger (אופציונלי)</h4>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
# Windows<br>
cd "C:\Users\haspe\OneDrive\Desktop\מהמחשב הישן\VScode\sasa_Software"<br>
sasa_env\Scripts\activate<br>
python logger-service/config_ui.py<br><br>

# פלט צפוי:<br>

# INFO: Uvicorn running on http://0.0.0.0:8081

</div>

<h4>טרמינל 4: ממשק הגדרות Watcher (אופציונלי)</h4>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
# Windows<br>
cd "C:\Users\haspe\OneDrive\Desktop\מהמחשב הישן\VScode\sasa_Software"<br>
sasa_env\Scripts\activate<br>
python watcher-service/config_ui.py<br><br>

# פלט צפוי:<br>

# INFO: Uvicorn running on http://0.0.0.0:8082

</div>

<h2>🧪 2.5 בדיקה ראשונה של המערכת ואימות</h2>

<h3>שלב 1: וודא שכל השירותים פועלים</h3>
<div style="background: #d4edda; padding: 15px; border-radius: 5px; border-right: 5px solid #28a745;">
<h4>📊 בדיקת סטטוס שירותים:</h4>
<table style="width: 100%; border-collapse: collapse; margin: 10px 0;">
    <thead style="background: #28a745; color: white;">
        <tr>
            <th style="padding: 8px; border: 1px solid #ddd;">שירות</th>
            <th style="padding: 8px; border: 1px solid #ddd;">URL</th>
            <th style="padding: 8px; border: 1px solid #ddd;">בדיקת סטטוס</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;">שירות הרישום</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><a href="http://localhost:8001">http://localhost:8001</a></td>
            <td style="padding: 8px; border: 1px solid #ddd;">✅ צריך להציג מסמכי FastAPI</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;">בדיקת בריאות</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><a href="http://localhost:8001/health">http://localhost:8001/health</a></td>
            <td style="padding: 8px; border: 1px solid #ddd;">✅ צריך להציג סטטוס JSON</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;">ממשק הגדרות Logger</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><a href="http://localhost:8081">http://localhost:8081</a></td>
            <td style="padding: 8px; border: 1px solid #ddd;">✅ צריך להציג טופס הגדרות</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;">ממשק הגדרות Watcher</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><a href="http://localhost:8082">http://localhost:8082</a></td>
            <td style="padding: 8px; border: 1px solid #ddd;">✅ צריך להציג טופס הגדרות</td>
        </tr>
    </tbody>
</table>
</div>

<h3>שלב 2: צור את קובץ הבדיקה הראשון שלך</h3>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
# Windows PowerShell<br>
echo "שלום SASA Software! זה קובץ הבדיקה הראשון שלי." > watched\my_first_test.txt<br><br>

# Linux/Mac<br>

echo "שלום SASA Software! זה קובץ הבדיקה הראשון שלי." > watched/my_first_test.txt<br><br>

# חלופה: צור עם כל עורך טקסט<br>

# פשוט שמור כל קובץ בתיקיית 'watched'

</div>

<h3>שלב 3: צפה בקסם קורה! 🎭</h3>
<div style="background: #e8f4fd; padding: 20px; border-radius: 8px; border-right: 5px solid #0066cc;">
<h4>🔍 מה אתה צריך לראות:</h4>
<ol>
    <li><strong>טרמינל שירות הצפייה:</strong>
        <pre>INFO: Added my_first_test.txt to processing queue
INFO: Processing file: ./watched/my_first_test.txt
INFO: Successfully sent metadata for my_first_test.txt
INFO: Moved my_first_test.txt to processed directory</pre>
    </li>
    <li><strong>טרמינל שירות הרישום:</strong>
        <pre>INFO: Incoming request: POST /log
INFO: Processing log request for file: my_first_test.txt
INFO: Successfully created log file: logs\my_first_test-20251003T123456Z.txt
INFO: Request completed: 200 in 0.005s</pre>
    </li>
</ol>
</div>

<h3>שלב 4: וודא תוצאות</h3>
<div style="background: #d4edda; padding: 15px; border-radius: 5px; border-right: 5px solid #28a745;">
<h4>📁 בדוק את המיקומים האלה:</h4>
<ol>
    <li><strong>תיקיית processed/:</strong> הקובץ המקורי שלך צריך להיות כאן</li>
    <li><strong>תיקיית logs/:</strong> קובץ לוג חדש עם חותמת זמן צריך להיווצר</li>
</ol>

<h4>📄 תוכן קובץ לוג לדוגמה:</h4>
<pre>Filename: my_first_test.txt
Size: 52B
Created At: 2025-10-03T12:34:56Z
Hash: a1b2c3d4e5f6789012345678901234567890abcd1234567890abcd1234567890
Processed At: 2025-10-03T12:34:58Z</pre>
</div>

<h3>שלב 5: בדוק ממשקי הגדרות</h3>
<div style="background: #fff3cd; padding: 15px; border-radius: 5px; border-right: 5px solid #ffc107;">
<ol>
    <li><strong>פתח ממשק הגדרות Logger:</strong> <a href="http://localhost:8081">http://localhost:8081</a>
        <ul>
            <li>✅ נסה לשנות תיקיית לוגים</li>
            <li>✅ שנה תבנית קובץ לוג</li>
            <li>✅ בדוק הגדרות התראות אימייל</li>
        </ul>
    </li>
    <li><strong>פתח ממשק הגדרות Watcher:</strong> <a href="http://localhost:8082">http://localhost:8082</a>
        <ul>
            <li>✅ שנה תיקיית צפייה</li>
            <li>✅ שנה תבניות קבצים</li>
            <li>✅ בדוק הגדרות ניסיון חוזר</li>
        </ul>
    </li>
</ol>
</div>

</div>

</div>

</div>

</body>
</html>
