# PROJECT 4 :🌨️ Weather API Automation 

### 📁 Project Overview
This project automatically fetches daily weather data using a public API, saves it as a CSV file with the date in its name, and emails it to you every day at 5 PM.
It’s also equipped with logging and can be scheduled to run automatically using Task Scheduler (Windows) or cron jobs (Linux/Mac).

---

### 🚀 Features

-Fetches weather data from a public API (e.g., Weatherapi).

-Stores the fetched data in a date-based CSV file (e.g., details24-10-25.csv).

-Automatically emails the CSV file every day.

-Logs all activities and errors for debugging or tracking.

-Can be scheduled to run daily using Task Scheduler.

---

### ⚙️ Setup Instructions

1️⃣ Install Required Packages
2️⃣ Get Your Weather API Key
3️⃣ Configure Email
4️⃣ Schedule the Script

    🪟 For Windows:

    Open Task Scheduler    
    Create a new task:    

    -Trigger: Daily at 5 PM    

    -Action: Start a program → python    

    -Arguments: Full path to your script    

    -Check “Run whether user is logged on or not”

---

### 🧠 Logging

Each run creates a log file (e.g., logs_24-10-25.log) with detailed information such as:

2025-10-24 17:00:01,203 - INFO - Script started
2025-10-24 17:00:03,912 - INFO - API call successful
2025-10-24 17:00:05,543 - INFO - Email sent successfully

This helps in tracking or debugging your automation.

---

### ✅ Future Enhancements

-Auto-delete log/CSV files older than 7 days

-Support multiple cities

-Include graphs (temperature trend, humidity variation, etc.)

-Send daily summary via WhatsApp or Telegram

---