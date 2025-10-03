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

</body>
</html>
