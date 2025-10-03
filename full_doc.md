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

<!-- SECTION 3: PROJECT STRUCTURE DEEP DIVE -->
<div class="page-break">
<h1 style="text-align: center; border-bottom: 3px solid #9b59b6; padding-bottom: 20px; color: #2c3e50;">
    📁 SECTION 3: PROJECT STRUCTURE DEEP DIVE<br>
    קטע 3: ניתוח מעמיק של מבנה הפרויקט
</h1>

<div class="bilingual-container">

<!-- ENGLISH SECTION -->
<div class="english-section">
<h2>📊 3.0 Project Structure Overview</h2>

<p>The SASA Software project follows a clean, organized microservices architecture. This section provides a comprehensive, line-by-line analysis of every file and directory in the project.</p>

<h3>📂 Complete Directory Tree:</h3>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace; font-size: 12px;">
<pre>
sasa_Software/
├── 📄 docker-compose.yml          # Docker orchestration configuration
├── 📄 requirements.txt            # Python dependencies
├── 📄 manage.py                   # System management script
├── 📄 run_services.py             # Alternative service runner
├── 📄 test_system.py              # System integration tests
├── 📄 validate_system.py          # System validation tool
├── 📄 .env.example                # Environment variables template
├── 
├── 🚀 start.sh                    # Linux/Mac startup script
├── 🚀 start.bat                   # Windows startup script
├── 🚀 start.ps1                   # PowerShell startup script
├── 🚀 start_windows.bat           # Alternative Windows script
│
├── 📁 shared/                     # Shared utilities and libraries
│   ├── jwt_manager.py            # JWT token management
│   └── utils.py                  # Common utility functions
│
├── 📁 watcher-service/           # File monitoring microservice
│   ├── watcher.py                # Main watcher service
│   ├── config_ui.py              # Configuration web interface
│   ├── config.yaml               # Service configuration
│   └── templates/
│       └── config_form.html      # UI template
│
├── 📁 logger-service/            # Logging microservice
│   ├── logger.py                 # Main logger service
│   ├── config_ui.py              # Configuration web interface
│   ├── config.yaml               # Service configuration
│   └── templates/
│       └── config_form.html      # UI template
│
├── 📁 watched/                   # Directory monitored for new files
├── 📁 processed/                 # Successfully processed files
├── 📁 logs/                      # Log files and service logs
└── 📁 temp/                      # Temporary files (created at runtime)
</pre>
</div>

<h3>🎯 Directory Purpose Summary:</h3>
<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
    <thead style="background: #9b59b6; color: white;">
        <tr>
            <th style="padding: 12px; border: 1px solid #ddd; text-align: left;">Directory/File</th>
            <th style="padding: 12px; border: 1px solid #ddd; text-align: left;">Type</th>
            <th style="padding: 12px; border: 1px solid #ddd; text-align: left;">Purpose</th>
        </tr>
    </thead>
    <tbody>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>docker-compose.yml</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Config</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Defines all services, networks, and volumes</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>requirements.txt</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Config</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Python package dependencies</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>manage.py</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Script</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Management CLI for system operations</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>shared/</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Module</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Common code used by both services</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>watcher-service/</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Service</td>
            <td style="padding: 8px; border: 1px solid #ddd;">File monitoring microservice</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>logger-service/</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Service</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Logging microservice</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>watched/</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Data</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Input directory for new files</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>processed/</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Data</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Archive for processed files</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>logs/</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Data</td>
            <td style="padding: 8px; border: 1px solid #ddd;">System and file logs</td>
        </tr>
    </tbody>
</table>

</div>

<!-- HEBREW SECTION -->
<div class="hebrew-section">
<h2>📊 3.0 סקירת מבנה הפרויקט</h2>

<p>פרויקט SASA Software עוקב אחר ארכיטקטורת מיקרו-שירותים נקייה ומאורגנת. חלק זה מספק ניתוח מקיף, שורה אחר שורה, של כל קובץ ותיקייה בפרויקט.</p>

<h3>📂 עץ תיקיות מלא:</h3>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace; font-size: 12px;">
<pre>
sasa_Software/
├── 📄 docker-compose.yml          # הגדרת תזמור Docker
├── 📄 requirements.txt            # תלויות Python
├── 📄 manage.py                   # סקריפט ניהול מערכת
├── 📄 run_services.py             # מריץ שירותים חלופי
├── 📄 test_system.py              # בדיקות אינטגרציה של מערכת
├── 📄 validate_system.py          # כלי אימות מערכת
├── 📄 .env.example                # תבנית משתני סביבה
├── 
├── 🚀 start.sh                    # סקריפט הפעלה Linux/Mac
├── 🚀 start.bat                   # סקריפט הפעלה Windows
├── 🚀 start.ps1                   # סקריפט הפעלה PowerShell
├── 🚀 start_windows.bat           # סקריפט Windows חלופי
│
├── 📁 shared/                     # כלי עזר וספריות משותפות
│   ├── jwt_manager.py            # ניהול אסימוני JWT
│   └── utils.py                  # פונקציות עזר משותפות
│
├── 📁 watcher-service/           # מיקרו-שירות ניטור קבצים
│   ├── watcher.py                # שירות צפייה ראשי
│   ├── config_ui.py              # ממשק ווב להגדרות
│   ├── config.yaml               # הגדרות שירות
│   └── templates/
│       └── config_form.html      # תבנית ממשק משתמש
│
├── 📁 logger-service/            # מיקרו-שירות רישום
│   ├── logger.py                 # שירות רישום ראשי
│   ├── config_ui.py              # ממשק ווב להגדרות
│   ├── config.yaml               # הגדרות שירות
│   └── templates/
│       └── config_form.html      # תבנית ממשק משתמש
│
├── 📁 watched/                   # תיקייה הנצפית לקבצים חדשים
├── 📁 processed/                 # קבצים שעובדו בהצלחה
├── 📁 logs/                      # קבצי לוג ולוגי שירותים
└── 📁 temp/                      # קבצים זמניים (נוצר בזמן ריצה)
</pre>
</div>

<h3>🎯 סיכום מטרות תיקיות:</h3>
<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
    <thead style="background: #9b59b6; color: white;">
        <tr>
            <th style="padding: 12px; border: 1px solid #ddd; text-align: right;">תיקייה/קובץ</th>
            <th style="padding: 12px; border: 1px solid #ddd; text-align: right;">סוג</th>
            <th style="padding: 12px; border: 1px solid #ddd; text-align: right;">מטרה</th>
        </tr>
    </thead>
    <tbody>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>docker-compose.yml</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">הגדרות</td>
            <td style="padding: 8px; border: 1px solid #ddd;">מגדיר את כל השירותים, רשתות ונפחים</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>requirements.txt</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">הגדרות</td>
            <td style="padding: 8px; border: 1px solid #ddd;">תלויות חבילות Python</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>manage.py</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">סקריפט</td>
            <td style="padding: 8px; border: 1px solid #ddd;">CLI ניהול לפעולות מערכת</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>shared/</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">מודול</td>
            <td style="padding: 8px; border: 1px solid #ddd;">קוד משותף המשמש את שני השירותים</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>watcher-service/</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">שירות</td>
            <td style="padding: 8px; border: 1px solid #ddd;">מיקרו-שירות ניטור קבצים</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>logger-service/</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">שירות</td>
            <td style="padding: 8px; border: 1px solid #ddd;">מיקרו-שירות רישום</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>watched/</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">נתונים</td>
            <td style="padding: 8px; border: 1px solid #ddd;">תיקיית קלט לקבצים חדשים</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>processed/</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">נתונים</td>
            <td style="padding: 8px; border: 1px solid #ddd;">ארכיון לקבצים מעובדים</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>logs/</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">נתונים</td>
            <td style="padding: 8px; border: 1px solid #ddd;">לוגים של מערכת וקבצים</td>
        </tr>
    </tbody>
</table>

</div>

</div>

<!-- SUBSECTION 3.1: ROOT DIRECTORY FILES -->
<div class="page-break">
<h2 style="text-align: center; border-bottom: 2px solid #9b59b6; padding-bottom: 15px;">
    3.1 Root Directory Files Analysis<br>
    ניתוח קבצי תיקיית השורש
</h2>

<div class="bilingual-container">

<!-- ENGLISH SECTION -->
<div class="english-section">
<h3>📄 3.1.1 docker-compose.yml - Container Orchestration</h3>

<h4>🎯 Purpose:</h4>
<p>This file defines the complete Docker environment for SASA Software. It orchestrates four separate containers that work together as a cohesive system.</p>

<h4>📋 File Structure Overview:</h4>
<div style="background: #e8f4fd; padding: 15px; border-radius: 5px; border-left: 5px solid #0066cc;">
<strong>Version:</strong> Docker Compose 3.8<br>
<strong>Services Defined:</strong> 4 containers<br>
<strong>Networks:</strong> 1 bridge network (sasa-network)<br>
<strong>Volumes:</strong> 3 named volumes<br>
<strong>Total Lines:</strong> 106 lines
</div>

<h4>🔍 Line-by-Line Analysis:</h4>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">Lines 1-3: Header and Version</h5>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>version: '3.8'

services:</code></pre>
<p><strong>Explanation:</strong></p>
<ul>
    <li><code>version: '3.8'</code> - Specifies Docker Compose file format version 3.8</li>
    <li>Version 3.8 supports all features we need: networks, volumes, health checks</li>
    <li><code>services:</code> - Begins the services section where all containers are defined</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">Lines 4-23: Logger Service Definition</h5>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>  logger-service:
    build:
      context: .
      dockerfile: Dockerfile.logger
    container_name: sasa-logger-service
    ports:
      - "8001:8001"
    volumes:
      - ./logs:/app/logs
      - ./logger-service/config.yaml:/app/logger-service/config.yaml
    environment:
      - JWT_SECRET=${JWT_SECRET:-sasa-Software2015}
      - SMTP_USER=${SMTP_USER:-}
      - SMTP_PASSWORD=${SMTP_PASSWORD:-}
    networks:
      - sasa-network
    restart: unless-stopped
    labels:
      - "com.sasa-software.service=logger"
      - "com.sasa-software.version=1.0.0"</code></pre>

<p><strong>Detailed Breakdown:</strong></p>
<ul>
    <li><strong>Line 4:</strong> <code>logger-service:</code> - Service name identifier</li>
    <li><strong>Lines 5-7:</strong> Build configuration
        <ul>
            <li><code>context: .</code> - Build from project root directory</li>
            <li><code>dockerfile: Dockerfile.logger</code> - Use specific Dockerfile for logger</li>
        </ul>
    </li>
    <li><strong>Line 8:</strong> <code>container_name: sasa-logger-service</code> - Friendly container name for easy identification</li>
    <li><strong>Lines 9-10:</strong> Port mapping
        <ul>
            <li><code>"8001:8001"</code> - Maps host port 8001 to container port 8001</li>
            <li>Logger API will be accessible at http://localhost:8001</li>
        </ul>
    </li>
    <li><strong>Lines 11-13:</strong> Volume mounts (data persistence)
        <ul>
            <li><code>./logs:/app/logs</code> - Logs directory shared between host and container</li>
            <li><code>./logger-service/config.yaml:/app/logger-service/config.yaml</code> - Config file mounted for easy editing</li>
        </ul>
    </li>
    <li><strong>Lines 14-17:</strong> Environment variables
        <ul>
            <li><code>JWT_SECRET</code> - Secret key for JWT token validation (default: sasa-Software2015)</li>
            <li><code>SMTP_USER</code> - Email username for notifications (optional)</li>
            <li><code>SMTP_PASSWORD</code> - Email password (optional)</li>
            <li>Syntax <code>${VAR:-default}</code> means: use VAR from .env file, or use default value</li>
        </ul>
    </li>
    <li><strong>Lines 18-19:</strong> <code>networks: sasa-network</code> - Connects to shared network for inter-service communication</li>
    <li><strong>Line 20:</strong> <code>restart: unless-stopped</code> - Auto-restart on failure, unless manually stopped</li>
    <li><strong>Lines 21-23:</strong> Labels for metadata and container management</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">Lines 25-48: Watcher Service Definition</h5>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>  watcher-service:
    build:
      context: .
      dockerfile: Dockerfile.watcher
    container_name: sasa-watcher-service
    ports:
      - "8000:8000"
    volumes:
      - ./watched:/app/watched
      - ./processed:/app/processed
      - ./logs:/app/logs
      - ./watcher-service/config.yaml:/app/watcher-service/config.yaml
    environment:
      - JWT_SECRET=${JWT_SECRET:-sasa-Software2015}
      - SMTP_USER=${SMTP_USER:-}
      - SMTP_PASSWORD=${SMTP_PASSWORD:-}
    networks:
      - sasa-network
    depends_on:
      - logger-service
    restart: unless-stopped
    labels:
      - "com.sasa-software.service=watcher"
      - "com.sasa-software.version=1.0.0"</code></pre>

<p><strong>Detailed Breakdown:</strong></p>
<ul>
    <li><strong>Lines 26-28:</strong> Build from Dockerfile.watcher</li>
    <li><strong>Line 31:</strong> <code>"8000:8000"</code> - Watcher health endpoint on port 8000</li>
    <li><strong>Lines 32-36:</strong> Volume mounts
        <ul>
            <li><code>./watched:/app/watched</code> - Input directory for new files</li>
            <li><code>./processed:/app/processed</code> - Output directory for processed files</li>
            <li><code>./logs:/app/logs</code> - Shared logs directory</li>
            <li><code>./watcher-service/config.yaml:/app/watcher-service/config.yaml</code> - Configuration</li>
        </ul>
    </li>
    <li><strong>Line 43-44:</strong> <code>depends_on: logger-service</code> - <strong>CRITICAL:</strong> Ensures logger starts before watcher</li>
    <li>This prevents connection errors when watcher tries to send data to logger</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">Lines 50-67: Watcher Config UI</h5>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>  watcher-config-ui:
    build:
      context: .
      dockerfile: Dockerfile.watcher
    container_name: sasa-watcher-config-ui
    ports:
      - "8080:8080"
    volumes:
      - ./watcher-service/config.yaml:/app/watcher-service/config.yaml
    environment:
      - JWT_SECRET=${JWT_SECRET:-sasa-Software2015}
    networks:
      - sasa-network
    command: ["python", "watcher-service/config_ui.py"]
    restart: unless-stopped
    labels:
      - "com.sasa-software.service=watcher-config-ui"
      - "com.sasa-software.version=1.0.0"</code></pre>

<p><strong>Key Points:</strong></p>
<ul>
    <li><strong>Line 56:</strong> <code>"8080:8080"</code> - Web UI accessible at http://localhost:8080</li>
    <li><strong>Line 63:</strong> <code>command:</code> - <strong>IMPORTANT:</strong> Overrides default container command</li>
    <li>Runs config_ui.py instead of watcher.py</li>
    <li>This allows us to use the same Docker image for both watcher service and its config UI</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">Lines 69-86: Logger Config UI</h5>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>  logger-config-ui:
    build:
      context: .
      dockerfile: Dockerfile.logger
    container_name: sasa-logger-config-ui
    ports:
      - "8081:8081"
    volumes:
      - ./logger-service/config.yaml:/app/logger-service/config.yaml
    environment:
      - JWT_SECRET=${JWT_SECRET:-sasa-Software2015}
    networks:
      - sasa-network
    command: ["python", "logger-service/config_ui.py"]
    restart: unless-stopped
    labels:
      - "com.sasa-software.service=logger-config-ui"
      - "com.sasa-software.version=1.0.0"</code></pre>

<p><strong>Key Points:</strong></p>
<ul>
    <li><strong>Line 75:</strong> <code>"8081:8081"</code> - Web UI accessible at http://localhost:8081</li>
    <li><strong>Line 82:</strong> Runs config_ui.py for logger configuration management</li>
    <li>Same pattern as watcher config UI - reuses the same Docker image</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">Lines 88-92: Network Definition</h5>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>networks:
  sasa-network:
    driver: bridge
    labels:
      - "com.sasa-software.network=main"</code></pre>

<p><strong>Explanation:</strong></p>
<ul>
    <li><code>sasa-network</code> - Custom bridge network for all services</li>
    <li><code>driver: bridge</code> - Standard Docker bridge network type</li>
    <li>All 4 containers can communicate with each other using service names</li>
    <li>Example: watcher-service can reach logger at <code>http://logger-service:8001</code></li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">Lines 94-106: Volume Definitions</h5>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>volumes:
  logs:
    driver: local
    labels:
      - "com.sasa-software.volume=logs"
  watched:
    driver: local
    labels:
      - "com.sasa-software.volume=watched"
  processed:
    driver: local
    labels:
      - "com.sasa-software.volume=processed"</code></pre>

<p><strong>Explanation:</strong></p>
<ul>
    <li>Defines three named volumes for data persistence</li>
    <li><code>driver: local</code> - Stores data on the host machine</li>
    <li>These volumes persist even if containers are removed</li>
    <li>Labels help with volume management and identification</li>
</ul>
</div>

<h4>🎯 Complete Service Communication Flow:</h4>
<div style="background: #e8f4fd; padding: 20px; border-radius: 8px; border-left: 5px solid #0066cc; margin: 20px 0;">
<pre style="font-family: 'Courier New', monospace; color: #2c3e50;">
┌─────────────────────┐
│   User's Browser    │
│   localhost:8080    │ ← Watcher Config UI
│   localhost:8081    │ ← Logger Config UI
└──────────┬──────────┘
           │
    ┌──────┴──────┐
    │             │
┌───▼────┐   ┌───▼────┐
│Config  │   │Config  │
│UI 8080 │   │UI 8081 │
└────────┘   └────────┘
           │
    ┌──────┴──────┐
    │             │
┌───▼────────┐   ┌───▼────────┐
│  Watcher   │──▶│   Logger   │
│  Service   │   │  Service   │
│  :8000     │   │  :8001     │
└────┬───────┘   └────┬───────┘
     │                │
     │                │
┌────▼──────┐   ┌────▼──────┐
│ ./watched │   │  ./logs   │
│./processed│   │           │
└───────────┘   └───────────┘
</pre>
</div>

</div>

<!-- HEBREW SECTION -->
<div class="hebrew-section">
<h3>📄 3.1.1 docker-compose.yml - תזמור מכולות</h3>

<h4>🎯 מטרה:</h4>
<p>קובץ זה מגדיר את סביבת Docker המלאה עבור SASA Software. הוא מתזמר ארבע מכולות נפרדות שעובדות ביחד כמערכת מגובשת.</p>

<h4>📋 סקירת מבנה הקובץ:</h4>
<div style="background: #e8f4fd; padding: 15px; border-radius: 5px; border-right: 5px solid #0066cc;">
<strong>גרסה:</strong> Docker Compose 3.8<br>
<strong>שירותים מוגדרים:</strong> 4 מכולות<br>
<strong>רשתות:</strong> רשת bridge אחת (sasa-network)<br>
<strong>נפחים:</strong> 3 נפחים עם שם<br>
<strong>סך שורות:</strong> 106 שורות
</div>

<h4>🔍 ניתוח שורה אחר שורה:</h4>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">שורות 1-3: כותרת וגרסה</h5>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>version: '3.8'

services:</code></pre>
<p><strong>הסבר:</strong></p>
<ul>
    <li><code>version: '3.8'</code> - מציין תבנית קובץ Docker Compose גרסה 3.8</li>
    <li>גרסה 3.8 תומכת בכל התכונות שאנו צריכים: רשתות, נפחים, בדיקות בריאות</li>
    <li><code>services:</code> - מתחיל את קטע השירותים שבו מוגדרות כל המכולות</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">שורות 4-23: הגדרת שירות Logger</h5>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>  logger-service:
    build:
      context: .
      dockerfile: Dockerfile.logger
    container_name: sasa-logger-service
    ports:
      - "8001:8001"
    volumes:
      - ./logs:/app/logs
      - ./logger-service/config.yaml:/app/logger-service/config.yaml
    environment:
      - JWT_SECRET=${JWT_SECRET:-sasa-Software2015}
      - SMTP_USER=${SMTP_USER:-}
      - SMTP_PASSWORD=${SMTP_PASSWORD:-}
    networks:
      - sasa-network
    restart: unless-stopped
    labels:
      - "com.sasa-software.service=logger"
      - "com.sasa-software.version=1.0.0"</code></pre>

<p><strong>פירוט מפורט:</strong></p>
<ul>
    <li><strong>שורה 4:</strong> <code>logger-service:</code> - מזהה שם שירות</li>
    <li><strong>שורות 5-7:</strong> הגדרות בנייה
        <ul>
            <li><code>context: .</code> - בנה מתיקיית שורש הפרויקט</li>
            <li><code>dockerfile: Dockerfile.logger</code> - השתמש ב-Dockerfile ספציפי עבור logger</li>
        </ul>
    </li>
    <li><strong>שורה 8:</strong> <code>container_name: sasa-logger-service</code> - שם מכולה ידידותי לזיהוי קל</li>
    <li><strong>שורות 9-10:</strong> מיפוי פורט
        <ul>
            <li><code>"8001:8001"</code> - ממפה פורט מארח 8001 לפורט מכולה 8001</li>
            <li>Logger API יהיה נגיש ב-http://localhost:8001</li>
        </ul>
    </li>
    <li><strong>שורות 11-13:</strong> עיגוני נפח (שמירת נתונים)
        <ul>
            <li><code>./logs:/app/logs</code> - תיקיית לוגים משותפת בין מארח למכולה</li>
            <li><code>./logger-service/config.yaml:/app/logger-service/config.yaml</code> - קובץ הגדרות מעוגן לעריכה קלה</li>
        </ul>
    </li>
    <li><strong>שורות 14-17:</strong> משתני סביבה
        <ul>
            <li><code>JWT_SECRET</code> - מפתח סודי לאימות אסימון JWT (ברירת מחדל: sasa-Software2015)</li>
            <li><code>SMTP_USER</code> - שם משתמש אימייל להתראות (אופציונלי)</li>
            <li><code>SMTP_PASSWORD</code> - סיסמת אימייל (אופציונלי)</li>
            <li>תחביר <code>${VAR:-default}</code> אומר: השתמש ב-VAR מקובץ .env, או השתמש בערך ברירת מחדל</li>
        </ul>
    </li>
    <li><strong>שורות 18-19:</strong> <code>networks: sasa-network</code> - מתחבר לרשת משותפת לתקשורת בין-שירותים</li>
    <li><strong>שורה 20:</strong> <code>restart: unless-stopped</code> - הפעלה אוטומטית מחדש בכישלון, אלא אם נעצר ידנית</li>
    <li><strong>שורות 21-23:</strong> תוויות למטא-נתונים וניהול מכולות</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">שורות 25-48: הגדרת שירות Watcher</h5>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>  watcher-service:
    build:
      context: .
      dockerfile: Dockerfile.watcher
    container_name: sasa-watcher-service
    ports:
      - "8000:8000"
    volumes:
      - ./watched:/app/watched
      - ./processed:/app/processed
      - ./logs:/app/logs
      - ./watcher-service/config.yaml:/app/watcher-service/config.yaml
    environment:
      - JWT_SECRET=${JWT_SECRET:-sasa-Software2015}
      - SMTP_USER=${SMTP_USER:-}
      - SMTP_PASSWORD=${SMTP_PASSWORD:-}
    networks:
      - sasa-network
    depends_on:
      - logger-service
    restart: unless-stopped
    labels:
      - "com.sasa-software.service=watcher"
      - "com.sasa-software.version=1.0.0"</code></pre>

<p><strong>פירוט מפורט:</strong></p>
<ul>
    <li><strong>שורות 26-28:</strong> בנה מ-Dockerfile.watcher</li>
    <li><strong>שורה 31:</strong> <code>"8000:8000"</code> - נקודת קצה בריאות Watcher על פורט 8000</li>
    <li><strong>שורות 32-36:</strong> עיגוני נפח
        <ul>
            <li><code>./watched:/app/watched</code> - תיקיית קלט לקבצים חדשים</li>
            <li><code>./processed:/app/processed</code> - תיקיית פלט לקבצים מעובדים</li>
            <li><code>./logs:/app/logs</code> - תיקיית לוגים משותפת</li>
            <li><code>./watcher-service/config.yaml:/app/watcher-service/config.yaml</code> - הגדרות</li>
        </ul>
    </li>
    <li><strong>שורות 43-44:</strong> <code>depends_on: logger-service</code> - <strong>קריטי:</strong> מבטיח ש-logger יתחיל לפני watcher</li>
    <li>זה מונע שגיאות חיבור כאשר watcher מנסה לשלוח נתונים ל-logger</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">שורות 50-67: ממשק הגדרות Watcher</h5>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>  watcher-config-ui:
    build:
      context: .
      dockerfile: Dockerfile.watcher
    container_name: sasa-watcher-config-ui
    ports:
      - "8080:8080"
    volumes:
      - ./watcher-service/config.yaml:/app/watcher-service/config.yaml
    environment:
      - JWT_SECRET=${JWT_SECRET:-sasa-Software2015}
    networks:
      - sasa-network
    command: ["python", "watcher-service/config_ui.py"]
    restart: unless-stopped
    labels:
      - "com.sasa-software.service=watcher-config-ui"
      - "com.sasa-software.version=1.0.0"</code></pre>

<p><strong>נקודות מפתח:</strong></p>
<ul>
    <li><strong>שורה 56:</strong> <code>"8080:8080"</code> - ממשק ווב נגיש ב-http://localhost:8080</li>
    <li><strong>שורה 63:</strong> <code>command:</code> - <strong>חשוב:</strong> עוקף את פקודת המכולה הברירת מחדל</li>
    <li>מריץ config_ui.py במקום watcher.py</li>
    <li>זה מאפשר לנו להשתמש באותה תמונת Docker גם לשירות watcher וגם לממשק ההגדרות שלו</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">שורות 69-86: ממשק הגדרות Logger</h5>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>  logger-config-ui:
    build:
      context: .
      dockerfile: Dockerfile.logger
    container_name: sasa-logger-config-ui
    ports:
      - "8081:8081"
    volumes:
      - ./logger-service/config.yaml:/app/logger-service/config.yaml
    environment:
      - JWT_SECRET=${JWT_SECRET:-sasa-Software2015}
    networks:
      - sasa-network
    command: ["python", "logger-service/config_ui.py"]
    restart: unless-stopped
    labels:
      - "com.sasa-software.service=logger-config-ui"
      - "com.sasa-software.version=1.0.0"</code></pre>

<p><strong>נקודות מפתח:</strong></p>
<ul>
    <li><strong>שורה 75:</strong> <code>"8081:8081"</code> - ממשק ווב נגיש ב-http://localhost:8081</li>
    <li><strong>שורה 82:</strong> מריץ config_ui.py לניהול הגדרות logger</li>
    <li>אותו תבנית כמו ממשק הגדרות watcher - משתמש מחדש באותה תמונת Docker</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">שורות 88-92: הגדרת רשת</h5>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>networks:
  sasa-network:
    driver: bridge
    labels:
      - "com.sasa-software.network=main"</code></pre>

<p><strong>הסבר:</strong></p>
<ul>
    <li><code>sasa-network</code> - רשת bridge מותאמת אישית לכל השירותים</li>
    <li><code>driver: bridge</code> - סוג רשת bridge סטנדרטי של Docker</li>
    <li>כל 4 המכולות יכולות לתקשר זו עם זו באמצעות שמות שירות</li>
    <li>דוגמה: watcher-service יכול להגיע ל-logger ב-<code>http://logger-service:8001</code></li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">שורות 94-106: הגדרות נפח</h5>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>volumes:
  logs:
    driver: local
    labels:
      - "com.sasa-software.volume=logs"
  watched:
    driver: local
    labels:
      - "com.sasa-software.volume=watched"
  processed:
    driver: local
    labels:
      - "com.sasa-software.volume=processed"</code></pre>

<p><strong>הסבר:</strong></p>
<ul>
    <li>מגדיר שלושה נפחים עם שם לשמירת נתונים</li>
    <li><code>driver: local</code> - מאחסן נתונים במכונת המארח</li>
    <li>נפחים אלה נשמרים גם אם המכולות מוסרות</li>
    <li>תוויות עוזרות בניהול נפחים וזיהוי</li>
</ul>
</div>

<h4>🎯 זרימת תקשורת שירות מלאה:</h4>
<div style="background: #e8f4fd; padding: 20px; border-radius: 8px; border-right: 5px solid #0066cc; margin: 20px 0;">
<pre style="font-family: 'Courier New', monospace; color: #2c3e50; direction: ltr;">
┌─────────────────────┐
│   User's Browser    │
│   localhost:8080    │ ← Watcher Config UI
│   localhost:8081    │ ← Logger Config UI
└──────────┬──────────┘
           │
    ┌──────┴──────┐
    │             │
┌───▼────┐   ┌───▼────┐
│Config  │   │Config  │
│UI 8080 │   │UI 8081 │
└────────┘   └────────┘
           │
    ┌──────┴──────┐
    │             │
┌───▼────────┐   ┌───▼────────┐
│  Watcher   │──▶│   Logger   │
│  Service   │   │  Service   │
│  :8000     │   │  :8001     │
└────┬───────┘   └────┬───────┘
     │                │
     │                │
┌────▼──────┐   ┌────▼──────┐
│ ./watched │   │  ./logs   │
│./processed│   │           │
└───────────┘   └───────────┘
</pre>
</div>

</div>

</div>

<!-- SUBSECTION 3.1.2: requirements.txt -->
<div class="page-break">
<h3 style="border-bottom: 2px solid #9b59b6; padding-bottom: 10px;">
    📄 3.1.2 requirements.txt - Python Dependencies<br>
    תלויות Python
</h3>

<div class="bilingual-container">

<!-- ENGLISH SECTION -->
<div class="english-section">
<h4>🎯 Purpose:</h4>
<p>Defines all Python packages required by the SASA Software system. This file is used by pip to install dependencies in Docker containers.</p>

<h4>📦 Complete Dependencies List:</h4>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>fastapi>=0.100.0
uvicorn>=0.20.0
watchdog>=3.0.0
pyjwt>=2.8.0
requests>=2.31.0
pydantic>=2.0.0
python-multipart>=0.0.6
jinja2>=3.1.0
aiofiles>=23.0.0
cryptography>=3.4.0
pyyaml>=6.0.0
python-dotenv>=1.0.0</code></pre>
</div>

<h4>📚 Package-by-Package Analysis:</h4>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">1. fastapi>=0.100.0</h5>
<p><strong>Category:</strong> Web Framework</p>
<p><strong>Purpose:</strong> Modern, fast web framework for building APIs</p>
<p><strong>Usage in SASA:</strong></p>
<ul>
    <li>Powers the Logger Service REST API (port 8001)</li>
    <li>Provides automatic API documentation via Swagger/OpenAPI</li>
    <li>Handles JWT authentication middleware</li>
    <li>Manages HTTP endpoints: <code>/log</code>, <code>/health</code></li>
</ul>
<p><strong>Why This Version:</strong> >=0.100.0 includes async/await improvements and better type hints</p>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">2. uvicorn>=0.20.0</h5>
<p><strong>Category:</strong> ASGI Server</p>
<p><strong>Purpose:</strong> Lightning-fast ASGI server implementation</p>
<p><strong>Usage in SASA:</strong></p>
<ul>
    <li>Runs the FastAPI applications</li>
    <li>Handles asynchronous request processing</li>
    <li>Serves both logger and watcher services</li>
    <li>Provides hot-reload during development</li>
</ul>
<p><strong>Key Features Used:</strong></p>
<ul>
    <li>HTTP/1.1 and WebSocket support</li>
    <li>Auto-reload for development</li>
    <li>Process management</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">3. watchdog>=3.0.0</h5>
<p><strong>Category:</strong> File System Monitoring</p>
<p><strong>Purpose:</strong> Cross-platform file system event monitoring</p>
<p><strong>Usage in SASA:</strong></p>
<ul>
    <li><strong>CRITICAL COMPONENT:</strong> The heart of the Watcher Service</li>
    <li>Monitors <code>./watched</code> directory for new files</li>
    <li>Triggers events on file creation, modification, deletion</li>
    <li>Works on Windows, Linux, and macOS</li>
</ul>
<p><strong>Implementation:</strong></p>
<ul>
    <li>Uses <code>FileSystemEventHandler</code> class</li>
    <li>Listens for <code>on_created</code> events</li>
    <li>Provides real-time file detection (< 1 second latency)</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">4. pyjwt>=2.8.0</h5>
<p><strong>Category:</strong> Security/Authentication</p>
<p><strong>Purpose:</strong> JSON Web Token implementation for Python</p>
<p><strong>Usage in SASA:</strong></p>
<ul>
    <li><strong>SECURITY CRITICAL:</strong> Secures inter-service communication</li>
    <li>Watcher creates JWT tokens before sending data to Logger</li>
    <li>Logger validates tokens before processing requests</li>
    <li>Uses HS256 algorithm with shared secret</li>
</ul>
<p><strong>Token Structure:</strong></p>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px;">
{
  "iss": "watcher-service",        # Issuer
  "exp": "2025-10-03T12:40:00Z",   # Expiration (5 minutes)
  "iat": "2025-10-03T12:35:00Z",   # Issued at
  "filename": "example.txt"         # Custom claims
}</pre>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">5. requests>=2.31.0</h5>
<p><strong>Category:</strong> HTTP Client</p>
<p><strong>Purpose:</strong> Simple, elegant HTTP requests library</p>
<p><strong>Usage in SASA:</strong></p>
<ul>
    <li>Watcher Service uses it to POST metadata to Logger Service</li>
    <li>Sends JWT token in Authorization header</li>
    <li>Handles HTTP responses and error codes</li>
    <li>Used by manage.py for health checks</li>
</ul>
<p><strong>Example Request:</strong></p>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px;">
headers = {"Authorization": f"Bearer {jwt_token}"}
response = requests.post(
    "http://logger-service:8001/log",
    json=metadata,
    headers=headers
)</pre>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">6. pydantic>=2.0.0</h5>
<p><strong>Category:</strong> Data Validation</p>
<p><strong>Purpose:</strong> Data validation using Python type hints</p>
<p><strong>Usage in SASA:</strong></p>
<ul>
    <li>Validates incoming JSON data structures</li>
    <li>Ensures file metadata has required fields</li>
    <li>Automatic data type conversion and validation</li>
    <li>FastAPI integration for request/response models</li>
</ul>
<p><strong>Example Model:</strong></p>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px;">
class FileMetadata(BaseModel):
    filename: str
    created_at: str
    file_size: int
    hash: str</pre>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">7. python-multipart>=0.0.6</h5>
<p><strong>Category:</strong> HTTP Parsing</p>
<p><strong>Purpose:</strong> Parse multipart/form-data requests</p>
<p><strong>Usage in SASA:</strong></p>
<ul>
    <li>Required by FastAPI for form handling</li>
    <li>Used in configuration UIs for form submissions</li>
    <li>Handles file uploads (if implemented)</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">8. jinja2>=3.1.0</h5>
<p><strong>Category:</strong> Template Engine</p>
<p><strong>Purpose:</strong> Modern template engine for Python</p>
<p><strong>Usage in SASA:</strong></p>
<ul>
    <li>Renders HTML templates for configuration UIs</li>
    <li>Used by both <code>watcher-service/config_ui.py</code> and <code>logger-service/config_ui.py</code></li>
    <li>Templates located in <code>*/templates/config_form.html</code></li>
    <li>Provides dynamic form generation with current config values</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">9. aiofiles>=23.0.0</h5>
<p><strong>Category:</strong> Async File I/O</p>
<p><strong>Purpose:</strong> Asynchronous file operations</p>
<p><strong>Usage in SASA:</strong></p>
<ul>
    <li>Non-blocking file reads and writes</li>
    <li>Used when reading file contents for hashing</li>
    <li>Improves performance by not blocking event loop</li>
    <li>Essential for handling multiple concurrent file operations</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">10. cryptography>=3.4.0</h5>
<p><strong>Category:</strong> Cryptography</p>
<p><strong>Purpose:</strong> Cryptographic recipes and primitives</p>
<p><strong>Usage in SASA:</strong></p>
<ul>
    <li>Required by PyJWT for certain algorithms</li>
    <li>Provides SHA256 hashing for file integrity</li>
    <li>Supports RSA and other encryption methods (if needed in future)</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">11. pyyaml>=6.0.0</h5>
<p><strong>Category:</strong> Configuration</p>
<p><strong>Purpose:</strong> YAML parser and emitter for Python</p>
<p><strong>Usage in SASA:</strong></p>
<ul>
    <li><strong>CRITICAL:</strong> Reads and writes all configuration files</li>
    <li>Both services use <code>config.yaml</code> files</li>
    <li>Configuration UIs read and update YAML files</li>
    <li>Provides human-readable configuration format</li>
</ul>
<p><strong>Example Usage:</strong></p>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px;">
import yaml
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)</pre>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">12. python-dotenv>=1.0.0</h5>
<p><strong>Category:</strong> Environment Management</p>
<p><strong>Purpose:</strong> Read key-value pairs from .env file</p>
<p><strong>Usage in SASA:</strong></p>
<ul>
    <li>Loads environment variables from <code>.env</code> file</li>
    <li>Manages secrets like JWT_SECRET, SMTP credentials</li>
    <li>Keeps sensitive data out of source code</li>
    <li>Docker Compose automatically uses .env file</li>
</ul>
</div>

<h4>📊 Dependency Category Summary:</h4>
<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
    <thead style="background: #9b59b6; color: white;">
        <tr>
            <th style="padding: 12px; border: 1px solid #ddd;">Category</th>
            <th style="padding: 12px; border: 1px solid #ddd;">Packages</th>
            <th style="padding: 12px; border: 1px solid #ddd;">Purpose</th>
        </tr>
    </thead>
    <tbody>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>Web Framework</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">fastapi, uvicorn</td>
            <td style="padding: 8px; border: 1px solid #ddd;">API endpoints and server</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>File Monitoring</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">watchdog, aiofiles</td>
            <td style="padding: 8px; border: 1px solid #ddd;">File system events and I/O</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>Security</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">pyjwt, cryptography</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Authentication and hashing</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>HTTP</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">requests, python-multipart</td>
            <td style="padding: 8px; border: 1px solid #ddd;">HTTP client and parsing</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>Data Handling</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">pydantic, pyyaml</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Validation and config</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>UI</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">jinja2</td>
            <td style="padding: 8px; border: 1px solid #ddd;">HTML templates</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>Environment</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">python-dotenv</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Environment variables</td>
        </tr>
    </tbody>
</table>

</div>

<!-- HEBREW SECTION -->
<div class="hebrew-section">
<h4>🎯 מטרה:</h4>
<p>מגדיר את כל חבילות Python הנדרשות על ידי מערכת SASA Software. קובץ זה משמש את pip להתקנת תלויות במכולות Docker.</p>

<h4>📦 רשימת תלויות מלאה:</h4>
<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>fastapi>=0.100.0
uvicorn>=0.20.0
watchdog>=3.0.0
pyjwt>=2.8.0
requests>=2.31.0
pydantic>=2.0.0
python-multipart>=0.0.6
jinja2>=3.1.0
aiofiles>=23.0.0
cryptography>=3.4.0
pyyaml>=6.0.0
python-dotenv>=1.0.0</code></pre>
</div>

<h4>📚 ניתוח חבילה אחר חבילה:</h4>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">1. fastapi>=0.100.0</h5>
<p><strong>קטגוריה:</strong> מסגרת ווב</p>
<p><strong>מטרה:</strong> מסגרת ווב מודרנית ומהירה לבניית APIs</p>
<p><strong>שימוש ב-SASA:</strong></p>
<ul>
    <li>מפעיל את Logger Service REST API (פורט 8001)</li>
    <li>מספק תיעוד API אוטומטי דרך Swagger/OpenAPI</li>
    <li>מטפל ב-middleware של אימות JWT</li>
    <li>מנהל נקודות קצה HTTP: <code>/log</code>, <code>/health</code></li>
</ul>
<p><strong>למה גרסה זו:</strong> >=0.100.0 כולל שיפורים ב-async/await ורמזי טיפוס טובים יותר</p>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">2. uvicorn>=0.20.0</h5>
<p><strong>קטגוריה:</strong> שרת ASGI</p>
<p><strong>מטרה:</strong> מימוש שרת ASGI מהיר במיוחד</p>
<p><strong>שימוש ב-SASA:</strong></p>
<ul>
    <li>מריץ את אפליקציות FastAPI</li>
    <li>מטפל בעיבוד בקשות אסינכרוני</li>
    <li>משרת גם את שירותי logger וגם watcher</li>
    <li>מספק טעינה חמה במהלך פיתוח</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">3. watchdog>=3.0.0</h5>
<p><strong>קטגוריה:</strong> ניטור מערכת קבצים</p>
<p><strong>מטרה:</strong> ניטור אירועי מערכת קבצים חוצה פלטפורמות</p>
<p><strong>שימוש ב-SASA:</strong></p>
<ul>
    <li><strong>רכיב קריטי:</strong> הלב של Watcher Service</li>
    <li>מנטר את תיקיית <code>./watched</code> לקבצים חדשים</li>
    <li>מפעיל אירועים ביצירה, שינוי, מחיקה של קבצים</li>
    <li>עובד על Windows, Linux ו-macOS</li>
</ul>
<p><strong>מימוש:</strong></p>
<ul>
    <li>משתמש במחלקה <code>FileSystemEventHandler</code></li>
    <li>מאזין לאירועי <code>on_created</code></li>
    <li>מספק זיהוי קבצים בזמן אמת (< שנייה אחת של עיכוב)</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">4. pyjwt>=2.8.0</h5>
<p><strong>קטגוריה:</strong> אבטחה/אימות</p>
<p><strong>מטרה:</strong> מימוש JSON Web Token עבור Python</p>
<p><strong>שימוש ב-SASA:</strong></p>
<ul>
    <li><strong>קריטי לאבטחה:</strong> מאבטח תקשורת בין-שירותית</li>
    <li>Watcher יוצר אסימוני JWT לפני שליחת נתונים ל-Logger</li>
    <li>Logger מאמת אסימונים לפני עיבוד בקשות</li>
    <li>משתמש באלגוריתם HS256 עם סוד משותף</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">5. requests>=2.31.0</h5>
<p><strong>קטגוריה:</strong> לקוח HTTP</p>
<p><strong>מטרה:</strong> ספריית בקשות HTTP פשוטה ואלגנטית</p>
<p><strong>שימוש ב-SASA:</strong></p>
<ul>
    <li>Watcher Service משתמש בה ל-POST מטא-נתונים ל-Logger Service</li>
    <li>שולח אסימון JWT בכותרת Authorization</li>
    <li>מטפל בתשובות HTTP וקודי שגיאה</li>
    <li>משמש את manage.py לבדיקות בריאות</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">11. pyyaml>=6.0.0</h5>
<p><strong>קטגוריה:</strong> הגדרות</p>
<p><strong>מטרה:</strong> מנתח ופולט YAML עבור Python</p>
<p><strong>שימוש ב-SASA:</strong></p>
<ul>
    <li><strong>קריטי:</strong> קורא וכותב את כל קבצי ההגדרות</li>
    <li>שני השירותים משתמשים בקבצי <code>config.yaml</code></li>
    <li>ממשקי ההגדרות קוראים ומעדכנים קבצי YAML</li>
    <li>מספק פורמט הגדרות קריא לאדם</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">12. python-dotenv>=1.0.0</h5>
<p><strong>קטגוריה:</strong> ניהול סביבה</p>
<p><strong>מטרה:</strong> קורא זוגות מפתח-ערך מקובץ .env</p>
<p><strong>שימוש ב-SASA:</strong></p>
<ul>
    <li>טוען משתני סביבה מקובץ <code>.env</code></li>
    <li>מנהל סודות כמו JWT_SECRET, אישורי SMTP</li>
    <li>שומר נתונים רגישים מחוץ לקוד מקור</li>
    <li>Docker Compose משתמש אוטומטית בקובץ .env</li>
</ul>
</div>

<h4>📊 סיכום קטגוריות תלויות:</h4>
<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
    <thead style="background: #9b59b6; color: white;">
        <tr>
            <th style="padding: 12px; border: 1px solid #ddd;">קטגוריה</th>
            <th style="padding: 12px; border: 1px solid #ddd;">חבילות</th>
            <th style="padding: 12px; border: 1px solid #ddd;">מטרה</th>
        </tr>
    </thead>
    <tbody>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>מסגרת ווב</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">fastapi, uvicorn</td>
            <td style="padding: 8px; border: 1px solid #ddd;">נקודות קצה API ושרת</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>ניטור קבצים</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">watchdog, aiofiles</td>
            <td style="padding: 8px; border: 1px solid #ddd;">אירועי מערכת קבצים ו-I/O</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>אבטחה</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">pyjwt, cryptography</td>
            <td style="padding: 8px; border: 1px solid #ddd;">אימות והצפנה</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>HTTP</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">requests, python-multipart</td>
            <td style="padding: 8px; border: 1px solid #ddd;">לקוח HTTP וניתוח</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>טיפול בנתונים</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">pydantic, pyyaml</td>
            <td style="padding: 8px; border: 1px solid #ddd;">אימות והגדרות</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>ממשק משתמש</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">jinja2</td>
            <td style="padding: 8px; border: 1px solid #ddd;">תבניות HTML</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>סביבה</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">python-dotenv</td>
            <td style="padding: 8px; border: 1px solid #ddd;">משתני סביבה</td>
        </tr>
    </tbody>
</table>

</div>

</div>

</div>

<!-- SUBSECTION 3.1.3: manage.py -->
<div class="page-break">
<h3 style="border-bottom: 2px solid #9b59b6; padding-bottom: 10px;">
    📄 3.1.3 manage.py - System Management Script<br>
    סקריפט ניהול מערכת
</h3>

<div class="bilingual-container">

<!-- ENGLISH SECTION -->
<div class="english-section">
<h4>🎯 Purpose:</h4>
<p>A comprehensive command-line management tool that provides easy-to-use commands for controlling, monitoring, and maintaining the SASA Software microservices system.</p>

<h4>📋 File Overview:</h4>
<div style="background: #e8f4fd; padding: 15px; border-radius: 5px; border-left: 5px solid #0066cc;">
<strong>Language:</strong> Python 3<br>
<strong>Total Lines:</strong> 219 lines<br>
<strong>Main Class:</strong> SASAManager<br>
<strong>Commands Available:</strong> 8 commands<br>
<strong>Usage:</strong> <code>python manage.py [command]</code>
</div>

<h4>📚 Available Commands:</h4>
<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
    <thead style="background: #9b59b6; color: white;">
        <tr>
            <th style="padding: 12px; border: 1px solid #ddd;">Command</th>
            <th style="padding: 12px; border: 1px solid #ddd;">Description</th>
            <th style="padding: 12px; border: 1px solid #ddd;">Example</th>
        </tr>
    </thead>
    <tbody>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><code>start</code></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Start all services</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>python manage.py start</code></td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>stop</code></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Stop all services</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>python manage.py stop</code></td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><code>restart</code></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Restart all services</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>python manage.py restart</code></td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>status</code></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Check service health</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>python manage.py status</code></td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><code>logs</code></td>
            <td style="padding: 8px; border: 1px solid #ddd;">View service logs</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>python manage.py logs -f</code></td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>stats</code></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Show system statistics</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>python manage.py stats</code></td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><code>cleanup</code></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Clean processed files</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>python manage.py cleanup</code></td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>test</code></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Run system tests</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>python manage.py test</code></td>
        </tr>
    </tbody>
</table>

<h4>🔍 Detailed Code Analysis:</h4>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">Lines 1-15: Imports and Header</h5>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>#!/usr/bin/env python3

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
from pathlib import Path</code></pre>
<p><strong>Line-by-Line Explanation:</strong></p>
<ul>
    <li><strong>Line 1:</strong> Shebang - makes script executable on Unix systems</li>
    <li><strong>Lines 3-6:</strong> Module docstring describing purpose</li>
    <li><strong>Line 8:</strong> <code>argparse</code> - Command-line argument parsing</li>
    <li><strong>Line 9-10:</strong> <code>os, sys</code> - Operating system and Python system interactions</li>
    <li><strong>Line 11:</strong> <code>subprocess</code> - Execute external commands (docker-compose)</li>
    <li><strong>Line 12:</strong> <code>time</code> - Delays and timing functions</li>
    <li><strong>Line 13:</strong> <code>requests</code> - HTTP client for health checks</li>
    <li><strong>Line 14:</strong> <code>pathlib.Path</code> - Modern path manipulation</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">Lines 16-24: SASAManager Class Initialization</h5>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>class SASAManager:
    """Management class for SASA Software services"""
    
    def __init__(self):
        self.services = {
            'logger': 'http://localhost:8001',
            'watcher-config': 'http://localhost:8080', 
            'logger-config': 'http://localhost:8081'
        }</code></pre>
<p><strong>Explanation:</strong></p>
<ul>
    <li><strong>Line 16:</strong> Defines the SASAManager class</li>
    <li><strong>Lines 19-24:</strong> Initializes service URLs dictionary
        <ul>
            <li><code>logger</code> - Logger service API endpoint</li>
            <li><code>watcher-config</code> - Watcher configuration UI</li>
            <li><code>logger-config</code> - Logger configuration UI</li>
        </ul>
    </li>
    <li>These URLs are used for health checks and status monitoring</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">Lines 26-33: check_docker() Method</h5>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>def check_docker(self):
    """Check if Docker is available"""
    try:
        subprocess.run(['docker', '--version'], capture_output=True, check=True)
        subprocess.run(['docker-compose', '--version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False</code></pre>
<p><strong>Purpose:</strong> Verify Docker and Docker Compose are installed</p>
<p><strong>How It Works:</strong></p>
<ul>
    <li><strong>Line 29:</strong> Runs <code>docker --version</code> command</li>
    <li><strong>Line 30:</strong> Runs <code>docker-compose --version</code> command</li>
    <li><code>capture_output=True</code> - Suppresses output to console</li>
    <li><code>check=True</code> - Raises exception if command fails</li>
    <li>Returns <code>True</code> if both commands succeed, <code>False</code> otherwise</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">Lines 35-61: start_services() Method</h5>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>def start_services(self):
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
        return False</code></pre>
<p><strong>Step-by-Step Process:</strong></p>
<ol>
    <li><strong>Line 39:</strong> Verify Docker is installed</li>
    <li><strong>Lines 44-47:</strong> Create required directories if they don't exist
        <ul>
            <li><code>exist_ok=True</code> - Don't error if directory exists</li>
        </ul>
    </li>
    <li><strong>Line 51:</strong> Execute <code>docker-compose up --build -d</code>
        <ul>
            <li><code>--build</code> - Rebuild images before starting</li>
            <li><code>-d</code> - Detached mode (run in background)</li>
        </ul>
    </li>
    <li><strong>Line 53:</strong> Wait 10 seconds for services to initialize</li>
    <li><strong>Line 56:</strong> Run health check on all services</li>
</ol>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">Lines 63-79: stop_services() and restart_services()</h5>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>def stop_services(self):
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
    return self.start_services()</code></pre>
<p><strong>Key Points:</strong></p>
<ul>
    <li><code>stop_services()</code> - Executes <code>docker-compose down</code></li>
    <li><code>restart_services()</code> - Stops services, waits 2 seconds, then starts them</li>
    <li>Error handling with try-except blocks</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">Lines 81-108: check_status() Method</h5>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>def check_status(self):
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
            print(f"❌ {name}: Not responding")</code></pre>
<p><strong>Functionality:</strong></p>
<ul>
    <li>Makes HTTP requests to each service's health endpoint</li>
    <li>For Logger Service: displays detailed health info including:
        <ul>
            <li>Service status</li>
            <li>Number of processed files</li>
            <li>Uptime in seconds</li>
        </ul>
    </li>
    <li>For Config UIs: simple up/down check</li>
    <li><code>timeout=5</code> - Wait max 5 seconds for response</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">Lines 123-152: show_stats() Method</h5>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>def show_stats(self):
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
        print(f"{name:15}: {status}")</code></pre>
<p><strong>What It Does:</strong></p>
<ol>
    <li>Counts files in watched/, processed/, and logs/ directories</li>
    <li>Displays file count for each directory</li>
    <li>Checks status of all services</li>
    <li>Formats output in a clean table format</li>
</ol>
<p><strong>Example Output:</strong></p>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px;">
📊 SASA Software Statistics
========================================
Watched     : 1 files
Processed   : 23 files
Logs        : 45 files

🔧 Service Status:
logger         : ✅ Running
watcher-config : ✅ Running
logger-config  : ✅ Running</pre>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">Lines 154-174: cleanup() Method</h5>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>def cleanup(self):
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
    
    print("✅ Cleanup completed")</code></pre>
<p><strong>Safety Features:</strong></p>
<ul>
    <li><strong>Line 158:</strong> Requires user confirmation before deletion</li>
    <li>Only cleans <code>processed/</code> and <code>logs/</code> directories</li>
    <li>Does NOT touch the <code>watched/</code> directory</li>
    <li>Reports number of files deleted from each directory</li>
</ul>
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">Lines 187-217: main() Function and Argument Parser</h5>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>def main():
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
    main()</code></pre>
<p><strong>Argument Parser Configuration:</strong></p>
<ul>
    <li><strong>Line 189:</strong> Creates argument parser with description</li>
    <li><strong>Lines 190-192:</strong> Defines required command argument with 8 choices</li>
    <li><strong>Line 194:</strong> Optional <code>--service</code> flag for logs command</li>
    <li><strong>Line 195:</strong> Optional <code>--follow</code> flag for tailing logs</li>
    <li><strong>Lines 201-216:</strong> Command dispatcher - routes to appropriate method</li>
</ul>
</div>

<h4>💡 Usage Examples:</h4>
<div style="background: #e8f4fd; padding: 20px; border-radius: 8px; border-left: 5px solid #0066cc; margin: 20px 0;">
<h5>Start System:</h5>
<pre>$ python manage.py start
🚀 Starting SASA Software services...
📁 Created directory: watched
📁 Created directory: processed
📁 Created directory: logs
📁 Created directory: temp
⏳ Waiting for services to start...
🔍 Checking service status...
✅ Logger Service: healthy
✅ Watcher Config UI: Running
✅ Logger Config UI: Running</pre>

<h5>Check Status:</h5>
<pre>$ python manage.py status
🔍 Checking service status...
✅ Logger Service: healthy
   Processed files: 23
   Uptime: 3600s
✅ Watcher Config UI: Running
✅ Logger Config UI: Running</pre>

<h5>View Statistics:</h5>
<pre>$ python manage.py stats
📊 SASA Software Statistics
========================================
Watched     : 1 files
Processed   : 23 files
Logs        : 45 files

🔧 Service Status:
logger         : ✅ Running
watcher-config : ✅ Running
logger-config  : ✅ Running</pre>

<h5>Follow Logs:</h5>
<pre>$ python manage.py logs --follow
# Shows real-time logs from all services</pre>
</div>

</div>

<!-- HEBREW SECTION -->
<div class="hebrew-section">
<h4>🎯 מטרה:</h4>
<p>כלי ניהול שורת פקודה מקיף המספק פקודות קלות לשימוש לשליטה, ניטור ותחזוקה של מערכת המיקרו-שירותים SASA Software.</p>

<h4>📋 סקירת קובץ:</h4>
<div style="background: #e8f4fd; padding: 15px; border-radius: 5px; border-right: 5px solid #0066cc;">
<strong>שפה:</strong> Python 3<br>
<strong>סך שורות:</strong> 219 שורות<br>
<strong>מחלקה ראשית:</strong> SASAManager<br>
<strong>פקודות זמינות:</strong> 8 פקודות<br>
<strong>שימוש:</strong> <code>python manage.py [command]</code>
</div>

<h4>📚 פקודות זמינות:</h4>
<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
    <thead style="background: #9b59b6; color: white;">
        <tr>
            <th style="padding: 12px; border: 1px solid #ddd;">פקודה</th>
            <th style="padding: 12px; border: 1px solid #ddd;">תיאור</th>
            <th style="padding: 12px; border: 1px solid #ddd;">דוגמה</th>
        </tr>
    </thead>
    <tbody>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><code>start</code></td>
            <td style="padding: 8px; border: 1px solid #ddd;">הפעל את כל השירותים</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>python manage.py start</code></td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>stop</code></td>
            <td style="padding: 8px; border: 1px solid #ddd;">עצור את כל השירותים</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>python manage.py stop</code></td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><code>restart</code></td>
            <td style="padding: 8px; border: 1px solid #ddd;">הפעל מחדש את כל השירותים</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>python manage.py restart</code></td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>status</code></td>
            <td style="padding: 8px; border: 1px solid #ddd;">בדוק בריאות שירות</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>python manage.py status</code></td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><code>logs</code></td>
            <td style="padding: 8px; border: 1px solid #ddd;">צפה בלוגים של שירות</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>python manage.py logs -f</code></td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>stats</code></td>
            <td style="padding: 8px; border: 1px solid #ddd;">הצג סטטיסטיקות מערכת</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>python manage.py stats</code></td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><code>cleanup</code></td>
            <td style="padding: 8px; border: 1px solid #ddd;">נקה קבצים מעובדים</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>python manage.py cleanup</code></td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>test</code></td>
            <td style="padding: 8px; border: 1px solid #ddd;">הפעל בדיקות מערכת</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>python manage.py test</code></td>
        </tr>
    </tbody>
</table>

<h4>🔍 תכונות עיקריות:</h4>
<ul>
    <li><strong>בדיקת Docker:</strong> מאמת התקנה לפני התחלה</li>
    <li><strong>יצירת תיקיות:</strong> יוצר אוטומטית תיקיות נדרשות</li>
    <li><strong>בדיקות בריאות:</strong> שאילתות HTTP לבדיקת סטטוס שירות</li>
    <li><strong>סטטיסטיקות:</strong> ספירת קבצים והצגת מידע מערכת</li>
    <li><strong>ניקוי בטוח:</strong> מחיקה מאושרת של קבצים</li>
    <li><strong>ניהול לוגים:</strong> צפייה ומעקב אחר לוגים</li>
    <li><strong>מימשק CLI:</strong> פקודות אינטואיטיביות עם עזרה</li>
    <li><strong>טיפול בשגיאות:</strong> הודעות שגיאה ברורות</li>
</ul>

<h4>💡 דוגמאות שימוש:</h4>
<div style="background: #e8f4fd; padding: 20px; border-radius: 8px; border-right: 5px solid #0066cc; margin: 20px 0;">
<h5>הפעלת מערכת:</h5>
<pre>$ python manage.py start
🚀 Starting SASA Software services...
📁 Created directory: watched
📁 Created directory: processed
📁 Created directory: logs
📁 Created directory: temp
⏳ Waiting for services to start...
🔍 Checking service status...
✅ Logger Service: healthy
✅ Watcher Config UI: Running
✅ Logger Config UI: Running</pre>

<h5>בדיקת סטטוס:</h5>
<pre>$ python manage.py status
🔍 Checking service status...
✅ Logger Service: healthy
   Processed files: 23
   Uptime: 3600s
✅ Watcher Config UI: Running
✅ Logger Config UI: Running</pre>
</div>

</div>

</div>

</div>

<!-- SUBSECTION 3.1.4: Startup Scripts -->
<div class="page-break">
<h3 style="border-bottom: 2px solid #9b59b6; padding-bottom: 10px;">
    📄 3.1.4 Startup Scripts - Quick Start Automation<br>
    סקריפטי הפעלה - אוטומציה להפעלה מהירה
</h3>

<div class="bilingual-container">

<!-- ENGLISH SECTION -->
<div class="english-section">
<h4>🎯 Purpose:</h4>
<p>Provide platform-specific startup scripts that automate the process of starting all SASA Software services. These scripts handle Docker orchestration and provide user-friendly output.</p>

<h4>📋 Available Startup Scripts:</h4>
<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
    <thead style="background: #9b59b6; color: white;">
        <tr>
            <th style="padding: 12px; border: 1px solid #ddd;">Script</th>
            <th style="padding: 12px; border: 1px solid #ddd;">Platform</th>
            <th style="padding: 12px; border: 1px solid #ddd;">Lines</th>
            <th style="padding: 12px; border: 1px solid #ddd;">Usage</th>
        </tr>
    </thead>
    <tbody>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>start.sh</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Linux / macOS</td>
            <td style="padding: 8px; border: 1px solid #ddd;">90 lines</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>./start.sh</code></td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>start.bat</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Windows (CMD)</td>
            <td style="padding: 8px; border: 1px solid #ddd;">89 lines</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>start.bat</code></td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>start.ps1</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Windows (PowerShell)</td>
            <td style="padding: 8px; border: 1px solid #ddd;">90 lines</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>.\start.ps1</code></td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>start_windows.bat</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Windows Alternative</td>
            <td style="padding: 8px; border: 1px solid #ddd;">~80 lines</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>start_windows.bat</code></td>
        </tr>
    </tbody>
</table>

<h4>🔍 Common Features Across All Scripts:</h4>
<div style="background: #e8f4fd; padding: 15px; border-radius: 5px; border-left: 5px solid #0066cc; margin: 20px 0;">
<h5>1. Docker Verification</h5>
<ul>
    <li>Checks if Docker is installed</li>
    <li>Verifies Docker Compose is available</li>
    <li>Exits with error message if not found</li>
</ul>

<h5>2. Environment File Setup</h5>
<ul>
    <li>Checks for <code>.env</code> file existence</li>
    <li>Creates from <code>.env.example</code> if missing</li>
    <li>Prompts user to configure before continuing</li>
</ul>

<h5>3. Directory Creation</h5>
<ul>
    <li>Creates <code>watched/</code>, <code>processed/</code>, <code>logs/</code>, <code>temp/</code> directories</li>
    <li>Safe creation (no error if exists)</li>
    <li>Reports directory creation status</li>
</ul>

<h5>4. Service Orchestration</h5>
<ul>
    <li>Stops any existing containers</li>
    <li>Builds and starts all services using Docker Compose</li>
    <li>Runs containers in detached mode (background)</li>
</ul>

<h5>5. Health Checks</h5>
<ul>
    <li>Waits 10 seconds for services to initialize</li>
    <li>Checks each service endpoint:
        <ul>
            <li>Logger Service: <code>http://localhost:8001/health</code></li>
            <li>Watcher Config UI: <code>http://localhost:8080/</code></li>
            <li>Logger Config UI: <code>http://localhost:8081/</code></li>
        </ul>
    </li>
    <li>Reports success/failure for each service</li>
</ul>

<h5>6. User Information</h5>
<ul>
    <li>Displays service endpoints</li>
    <li>Shows directory locations</li>
    <li>Provides management commands</li>
    <li>Gives usage instructions</li>
</ul>
</div>

<h4>📝 Detailed Analysis: start.sh (Linux/macOS)</h4>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">Key Sections:</h5>

<h6>Lines 1-17: Docker Verification</h6>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>#!/bin/bash

echo "🚀 Starting SASA Software Microservices..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi</code></pre>
<p><strong>Explanation:</strong></p>
<ul>
    <li><code>#!/bin/bash</code> - Bash shebang for script execution</li>
    <li><code>command -v docker</code> - Checks if docker command exists</li>
    <li><code>&> /dev/null</code> - Redirects all output to null (silences output)</li>
    <li><code>exit 1</code> - Exits with error code 1 on failure</li>
</ul>

<h6>Lines 19-25: Environment File Check</h6>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code># Check if .env file exists, if not create from example
if [ ! -f .env ]; then
    echo "📝 Creating .env file from example..."
    cp .env.example .env
    echo "✅ Please edit .env file with your configuration before running again."
    exit 1
fi</code></pre>
<p><strong>Safety Feature:</strong> Prevents running without proper configuration</p>

<h6>Lines 27-28: Directory Creation</h6>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code># Create directories if they don't exist
mkdir -p watched processed logs temp</code></pre>
<p><strong>Note:</strong> <code>-p</code> flag creates parent directories and doesn't error if exists</p>

<h6>Lines 30-36: Docker Compose Commands</h6>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code># Stop any existing containers
echo "🛑 Stopping existing containers..."
docker-compose down

# Build and start services
echo "🔨 Building and starting services..."
docker-compose up --build -d</code></pre>
<p><strong>Commands:</strong></p>
<ul>
    <li><code>docker-compose down</code> - Stops and removes containers</li>
    <li><code>docker-compose up --build -d</code> - Builds images and starts containers in background</li>
</ul>

<h6>Lines 46-70: Health Check Logic</h6>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code># Check Logger Service
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
fi</code></pre>
<p><strong>How It Works:</strong></p>
<ul>
    <li><code>curl -s</code> - Silent mode (no progress bar)</li>
    <li><code>> /dev/null</code> - Discard output, only check exit code</li>
    <li>Exit code 0 = success, non-zero = failure</li>
</ul>
</div>

<h4>📝 Detailed Analysis: start.bat (Windows CMD)</h4>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">Key Differences from Bash Version:</h5>

<h6>Docker Check (Windows Style):</h6>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>@echo off
echo 🚀 Starting SASA Software Microservices...

REM Check if Docker is installed
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker is not installed. Please install Docker first.
    exit /b 1
)</code></pre>
<p><strong>Windows Specifics:</strong></p>
<ul>
    <li><code>@echo off</code> - Disables command echoing</li>
    <li><code>REM</code> - Comment syntax in batch files</li>
    <li><code>>nul 2>&1</code> - Redirects both stdout and stderr to null</li>
    <li><code>%errorlevel%</code> - Exit code of last command</li>
    <li><code>exit /b 1</code> - Exits batch file with code 1</li>
</ul>

<h6>Directory Creation:</h6>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>REM Create directories if they don't exist
if not exist watched mkdir watched
if not exist processed mkdir processed
if not exist logs mkdir logs
if not exist temp mkdir temp</code></pre>

<h6>Health Check with curl:</h6>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>curl -s http://localhost:8001/health >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Logger Service is running on http://localhost:8001
) else (
    echo ❌ Logger Service failed to start
)</code></pre>

<h6>Pause at End:</h6>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>pause</code></pre>
<p><strong>Purpose:</strong> Keeps window open so user can read output</p>
</div>

<h4>📝 Detailed Analysis: start.ps1 (PowerShell)</h4>

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h5 style="color: #9b59b6;">PowerShell-Specific Features:</h5>

<h6>Colored Output:</h6>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>Write-Host "🚀 Starting SASA Software Microservices..." -ForegroundColor Green
Write-Host "❌ Docker is not installed." -ForegroundColor Red
Write-Host "📦 Installing Python dependencies..." -ForegroundColor Yellow</code></pre>
<p><strong>Colors Used:</strong></p>
<ul>
    <li>Green - Success messages</li>
    <li>Red - Error messages</li>
    <li>Yellow - Warning/info messages</li>
    <li>Cyan - Headers/labels</li>
</ul>

<h6>Try-Catch Error Handling:</h6>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python found: $pythonVersion" -ForegroundColor Green
}
catch {
    Write-Host "❌ Python is not installed." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}</code></pre>

<h6>Directory Creation with Arrays:</h6>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>$directories = @("watched", "processed", "logs", "temp")
foreach ($dir in $directories) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir | Out-Null
        Write-Host "📁 Created directory: $dir" -ForegroundColor Cyan
    }
}</code></pre>

<h6>HTTP Request with PowerShell:</h6>
<pre style="background: #2d2d2d; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto;">
<code>try {
    $response = Invoke-WebRequest -Uri "http://localhost:8001/health" -TimeoutSec 5 -ErrorAction Stop
    Write-Host "✅ Logger Service is running" -ForegroundColor Green
}
catch {
    Write-Host "⚠️ Logger Service may not be ready yet" -ForegroundColor Yellow
}</code></pre>
</div>

<h4>📊 Comparison Matrix:</h4>
<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
    <thead style="background: #9b59b6; color: white;">
        <tr>
            <th style="padding: 12px; border: 1px solid #ddd;">Feature</th>
            <th style="padding: 12px; border: 1px solid #ddd;">start.sh</th>
            <th style="padding: 12px; border: 1px solid #ddd;">start.bat</th>
            <th style="padding: 12px; border: 1px solid #ddd;">start.ps1</th>
        </tr>
    </thead>
    <tbody>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>Platform</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Linux/macOS</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Windows CMD</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Windows PS</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>Colored Output</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Emoji only</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Emoji only</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Full color</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>Error Handling</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Exit codes</td>
            <td style="padding: 8px; border: 1px solid #ddd;">errorlevel</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Try-Catch</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>HTTP Checks</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">curl</td>
            <td style="padding: 8px; border: 1px solid #ddd;">curl</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Invoke-WebRequest</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>User Experience</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Good</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Good</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Best</td>
        </tr>
    </tbody>
</table>

<h4>💡 Usage Recommendations:</h4>
<div style="background: #d4edda; padding: 15px; border-radius: 5px; border-left: 5px solid #28a745; margin: 20px 0;">
<ul>
    <li><strong>Linux/macOS:</strong> Use <code>start.sh</code> - Native and efficient</li>
    <li><strong>Windows 10+:</strong> Use <code>start.ps1</code> - Best features and error handling</li>
    <li><strong>Windows (older):</strong> Use <code>start.bat</code> - Compatible with all Windows versions</li>
    <li><strong>First Time:</strong> Make sure to edit <code>.env</code> file with your settings</li>
</ul>
</div>

</div>

<!-- HEBREW SECTION -->
<div class="hebrew-section">
<h4>🎯 מטרה:</h4>
<p>לספק סקריפטי הפעלה ספציפיים לפלטפורמה שמאוטמטים את תהליך הפעלת כל שירותי SASA Software. סקריפטים אלה מטפלים בתזמור Docker ומספקים פלט ידידותי למשתמש.</p>

<h4>📋 סקריפטי הפעלה זמינים:</h4>
<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
    <thead style="background: #9b59b6; color: white;">
        <tr>
            <th style="padding: 12px; border: 1px solid #ddd;">סקריפט</th>
            <th style="padding: 12px; border: 1px solid #ddd;">פלטפורמה</th>
            <th style="padding: 12px; border: 1px solid #ddd;">שורות</th>
            <th style="padding: 12px; border: 1px solid #ddd;">שימוש</th>
        </tr>
    </thead>
    <tbody>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>start.sh</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Linux / macOS</td>
            <td style="padding: 8px; border: 1px solid #ddd;">90 שורות</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>./start.sh</code></td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>start.bat</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Windows (CMD)</td>
            <td style="padding: 8px; border: 1px solid #ddd;">89 שורות</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>start.bat</code></td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>start.ps1</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Windows (PowerShell)</td>
            <td style="padding: 8px; border: 1px solid #ddd;">90 שורות</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>.\start.ps1</code></td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>start_windows.bat</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Windows חלופי</td>
            <td style="padding: 8px; border: 1px solid #ddd;">~80 שורות</td>
            <td style="padding: 8px; border: 1px solid #ddd;"><code>start_windows.bat</code></td>
        </tr>
    </tbody>
</table>

<h4>🔍 תכונות משותפות בכל הסקריפטים:</h4>
<div style="background: #e8f4fd; padding: 15px; border-radius: 5px; border-right: 5px solid #0066cc; margin: 20px 0;">
<h5>1. אימות Docker</h5>
<ul>
    <li>בודק אם Docker מותקן</li>
    <li>מאמת ש-Docker Compose זמין</li>
    <li>יוצא עם הודעת שגיאה אם לא נמצא</li>
</ul>

<h5>2. הגדרת קובץ סביבה</h5>
<ul>
    <li>בודק קיום קובץ <code>.env</code></li>
    <li>יוצר מ-<code>.env.example</code> אם חסר</li>
    <li>מבקש מהמשתמש להגדיר לפני המשך</li>
</ul>

<h5>3. יצירת תיקיות</h5>
<ul>
    <li>יוצר תיקיות <code>watched/</code>, <code>processed/</code>, <code>logs/</code>, <code>temp/</code></li>
    <li>יצירה בטוחה (אין שגיאה אם קיים)</li>
    <li>מדווח על סטטוס יצירת תיקיה</li>
</ul>

<h5>4. תזמור שירותים</h5>
<ul>
    <li>עוצר כל מכולות קיימות</li>
    <li>בונה ומפעיל את כל השירותים באמצעות Docker Compose</li>
    <li>מריץ מכולות במצב מנותק (רקע)</li>
</ul>

<h5>5. בדיקות בריאות</h5>
<ul>
    <li>ממתין 10 שניות לאתחול שירותים</li>
    <li>בודק כל נקודת קצה של שירות</li>
    <li>מדווח הצלחה/כישלון לכל שירות</li>
</ul>

<h5>6. מידע למשתמש</h5>
<ul>
    <li>מציג נקודות קצה של שירות</li>
    <li>מראה מיקומי תיקיות</li>
    <li>מספק פקודות ניהול</li>
    <li>נותן הוראות שימוש</li>
</ul>
</div>

<h4>📊 מטריצת השוואה:</h4>
<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
    <thead style="background: #9b59b6; color: white;">
        <tr>
            <th style="padding: 12px; border: 1px solid #ddd;">תכונה</th>
            <th style="padding: 12px; border: 1px solid #ddd;">start.sh</th>
            <th style="padding: 12px; border: 1px solid #ddd;">start.bat</th>
            <th style="padding: 12px; border: 1px solid #ddd;">start.ps1</th>
        </tr>
    </thead>
    <tbody>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>פלטפורמה</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">Linux/macOS</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Windows CMD</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Windows PS</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>פלט צבעוני</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">רק אמוג'י</td>
            <td style="padding: 8px; border: 1px solid #ddd;">רק אמוג'י</td>
            <td style="padding: 8px; border: 1px solid #ddd;">צבע מלא</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>טיפול בשגיאות</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">קודי יציאה</td>
            <td style="padding: 8px; border: 1px solid #ddd;">errorlevel</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Try-Catch</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>בדיקות HTTP</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">curl</td>
            <td style="padding: 8px; border: 1px solid #ddd;">curl</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Invoke-WebRequest</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>חוויית משתמש</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">טובה</td>
            <td style="padding: 8px; border: 1px solid #ddd;">טובה</td>
            <td style="padding: 8px; border: 1px solid #ddd;">הטובה ביותר</td>
        </tr>
    </tbody>
</table>

<h4>💡 המלצות שימוש:</h4>
<div style="background: #d4edda; padding: 15px; border-radius: 5px; border-right: 5px solid #28a745; margin: 20px 0;">
<ul>
    <li><strong>Linux/macOS:</strong> השתמש ב-<code>start.sh</code> - מקורי ויעיל</li>
    <li><strong>Windows 10+:</strong> השתמש ב-<code>start.ps1</code> - תכונות ולטיפול בשגיאות הטוב ביותר</li>
    <li><strong>Windows (ישן יותר):</strong> השתמש ב-<code>start.bat</code> - תואם לכל גרסאות Windows</li>
    <li><strong>פעם ראשונה:</strong> וודא לערוך את קובץ <code>.env</code> עם ההגדרות שלך</li>
</ul>
</div>

</div>

</div>

<!-- SECTION 3.1 SUMMARY -->
<div class="page-break">
<h2 style="text-align: center; border-bottom: 2px solid #9b59b6; padding-bottom: 15px;">
    📋 Section 3.1 Summary - Root Directory Files<br>
    סיכום סעיף 3.1 - קבצי תיקיית השורש
</h2>

<div class="bilingual-container">

<!-- ENGLISH SECTION -->
<div class="english-section">
<h3>🎯 What We've Covered:</h3>
<p>We've completed an in-depth analysis of all root directory files that control system orchestration, dependencies, management, and startup automation.</p>

<h4>📊 Files Analyzed:</h4>
<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
    <thead style="background: #9b59b6; color: white;">
        <tr>
            <th style="padding: 12px; border: 1px solid #ddd;">File</th>
            <th style="padding: 12px; border: 1px solid #ddd;">Lines</th>
            <th style="padding: 12px; border: 1px solid #ddd;">Purpose</th>
            <th style="padding: 12px; border: 1px solid #ddd;">Importance</th>
        </tr>
    </thead>
    <tbody>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>docker-compose.yml</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">106</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Container orchestration</td>
            <td style="padding: 8px; border: 1px solid #ddd;">⭐⭐⭐⭐⭐</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>requirements.txt</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">12</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Python dependencies</td>
            <td style="padding: 8px; border: 1px solid #ddd;">⭐⭐⭐⭐⭐</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>manage.py</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">219</td>
            <td style="padding: 8px; border: 1px solid #ddd;">System management CLI</td>
            <td style="padding: 8px; border: 1px solid #ddd;">⭐⭐⭐⭐</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>start.sh/bat/ps1</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">~90</td>
            <td style="padding: 8px; border: 1px solid #ddd;">Startup automation</td>
            <td style="padding: 8px; border: 1px solid #ddd;">⭐⭐⭐⭐</td>
        </tr>
    </tbody>
</table>

<h4>🔑 Key Takeaways:</h4>
<ol>
    <li><strong>Docker Compose</strong> is the backbone of service orchestration
        <ul>
            <li>4 services: logger, watcher, and 2 config UIs</li>
            <li>1 custom network for inter-service communication</li>
            <li>3 persistent volumes for data retention</li>
        </ul>
    </li>
    <li><strong>Python Dependencies</strong> are carefully chosen
        <ul>
            <li>12 packages covering web, security, file monitoring, and data handling</li>
            <li>All modern, well-maintained libraries</li>
            <li>Minimal footprint for efficient containers</li>
        </ul>
    </li>
    <li><strong>Management Tools</strong> provide flexibility
        <ul>
            <li>Python CLI (manage.py) for cross-platform management</li>
            <li>Platform-specific startup scripts for easy deployment</li>
            <li>8 management commands covering all operations</li>
        </ul>
    </li>
</ol>

<h4>🎓 Skills You've Learned:</h4>
<div style="background: #d4edda; padding: 15px; border-radius: 5px; border-left: 5px solid #28a745;">
<ul>
    <li>✅ How to read and understand Docker Compose configurations</li>
    <li>✅ Purpose and role of each Python package</li>
    <li>✅ System management with command-line tools</li>
    <li>✅ Cross-platform scripting differences and best practices</li>
    <li>✅ Service orchestration and health checking</li>
</ul>
</div>

<h4>📌 Next Section Preview:</h4>
<p>In Section 3.2, we'll dive deep into the <code>shared/</code> directory, examining common utilities used by both services:</p>
<ul>
    <li>📄 <code>jwt_manager.py</code> - JWT token creation and validation</li>
    <li>📄 <code>utils.py</code> - Configuration management, notifications, and logging utilities</li>
</ul>

</div>

<!-- HEBREW SECTION -->
<div class="hebrew-section">
<h3>🎯 מה כיסינו:</h3>
<p>השלמנו ניתוח מעמיק של כל קבצי תיקיית השורש השולטים בתזמור מערכת, תלויות, ניהול ואוטומציה של הפעלה.</p>

<h4>📊 קבצים שנותחו:</h4>
<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
    <thead style="background: #9b59b6; color: white;">
        <tr>
            <th style="padding: 12px; border: 1px solid #ddd;">קובץ</th>
            <th style="padding: 12px; border: 1px solid #ddd;">שורות</th>
            <th style="padding: 12px; border: 1px solid #ddd;">מטרה</th>
            <th style="padding: 12px; border: 1px solid #ddd;">חשיבות</th>
        </tr>
    </thead>
    <tbody>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>docker-compose.yml</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">106</td>
            <td style="padding: 8px; border: 1px solid #ddd;">תזמור מכולות</td>
            <td style="padding: 8px; border: 1px solid #ddd;">⭐⭐⭐⭐⭐</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>requirements.txt</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">12</td>
            <td style="padding: 8px; border: 1px solid #ddd;">תלויות Python</td>
            <td style="padding: 8px; border: 1px solid #ddd;">⭐⭐⭐⭐⭐</td>
        </tr>
        <tr style="background: #f8f9fa;">
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>manage.py</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">219</td>
            <td style="padding: 8px; border: 1px solid #ddd;">CLI ניהול מערכת</td>
            <td style="padding: 8px; border: 1px solid #ddd;">⭐⭐⭐⭐</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #ddd;"><strong>start.sh/bat/ps1</strong></td>
            <td style="padding: 8px; border: 1px solid #ddd;">~90</td>
            <td style="padding: 8px; border: 1px solid #ddd;">אוטומציה של הפעלה</td>
            <td style="padding: 8px; border: 1px solid #ddd;">⭐⭐⭐⭐</td>
        </tr>
    </tbody>
</table>

<h4>🔑 נקודות מפתח:</h4>
<ol>
    <li><strong>Docker Compose</strong> הוא עמוד השדרה של תזמור שירותים
        <ul>
            <li>4 שירותים: logger, watcher, ו-2 ממשקי הגדרות</li>
            <li>רשת מותאמת אישית אחת לתקשורת בין-שירותית</li>
            <li>3 נפחים מתמשכים לשמירת נתונים</li>
        </ul>
    </li>
    <li><strong>תלויות Python</strong> נבחרו בקפידה
        <ul>
            <li>12 חבילות המכסות ווב, אבטחה, ניטור קבצים וטיפול בנתונים</li>
            <li>כל הספריות מודרניות ומתוחזקות היטב</li>
            <li>טביעת רגל מינימלית למכולות יעילות</li>
        </ul>
    </li>
    <li><strong>כלי ניהול</strong> מספקים גמישות
        <ul>
            <li>Python CLI (manage.py) לניהול חוצה פלטפורמות</li>
            <li>סקריפטי הפעלה ספציפיים לפלטפורמה לפריסה קלה</li>
            <li>8 פקודות ניהול המכסות את כל הפעולות</li>
        </ul>
    </li>
</ol>

<h4>🎓 מיומנויות שלמדת:</h4>
<div style="background: #d4edda; padding: 15px; border-radius: 5px; border-right: 5px solid #28a745;">
<ul>
    <li>✅ איך לקרוא ולהבין הגדרות Docker Compose</li>
    <li>✅ מטרה ותפקיד של כל חבילת Python</li>
    <li>✅ ניהול מערכת עם כלי שורת פקודה</li>
    <li>✅ הבדלי סקריפטים חוצי פלטפורמות ושיטות עבודה מומלצות</li>
    <li>✅ תזמור שירותים ובדיקות בריאות</li>
</ul>
</div>

<h4>📌 תצוגה מקדימה של הסעיף הבא:</h4>
<p>בסעיף 3.2, נצלול לעומק לתוך תיקיית <code>shared/</code>, ונבחן כלי עזר משותפים המשמשים את שני השירותים:</p>
<ul>
    <li>📄 <code>jwt_manager.py</code> - יצירה ואימות אסימוני JWT</li>
    <li>📄 <code>utils.py</code> - ניהול הגדרות, התראות וכלי רישום</li>
</ul>

</div>

</div>

</div>

</body>
</html>
