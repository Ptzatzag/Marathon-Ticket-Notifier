## Marathon Ticket Availability Tracker
This repository contains a simple Python script that checks when the resale ticket platform for the Copenhagen Marathon goes live. It was built as a personal learning project in automation and scheduling, and can be used as a lightweight notifier when tickets appear.

## 📁 Repository Contents
- **`tracker.py`**,    Script that monitors the resale platform’s main page and notifies on changes or when “resale” is mentioned
- **`scheduler.bat`**,    Windows batch file that allows the script to run automatically when your computer reboots 

## ⚙️ Requirements
- `Python 3.8+`
- `Requests` and `Beautifulsoup4`

## 🚀 Run
### Manually 
```
python tracker.py
```

### Automate
1. For windows, press `Win+R` and type:
```
shell:startup
```
2. Copy the **`scheduler.bat`**
3. The script will now run automatically each time you start your computer.

## 📝 Notes
- The script is configured to check publicly available information only
- You can adapt it to send notifications (e.g., email, desktop alerts, or logging) depending on your preference
- Be mindful of how often you query the website, avoid sending excessive requests

## ⚠️ Disclaimer
This project is for personal and educational use only.
It is not affiliated with or endorsed by the Copenhagen Marathon or its ticketing partners. Please respect the website’s Terms of Service and use responsibly.
