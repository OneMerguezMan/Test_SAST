# Vulnerable Flask App for DAST Testing  

This is a deliberately vulnerable web application built with Flask, designed to test DAST (Dynamic Application Security Testing) tools. **Do not deploy in production!**

## Vulnerabilities Included
- SQL Injection
- Cross-Site Scripting (XSS)
- Command Injection
- Insecure Direct Object Reference (IDOR)
- File Upload Vulnerability
- Sensitive Data Exposure
- Open Redirect

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the app:
   ```bash
   python app.py
   ```
3. Access the app at [http://localhost:5000](http://localhost:5000)

## Features
- `/login` - SQL Injection
- `/greet?name=...` - XSS
- `/ping` - Command Injection
- `/note/<id>` - IDOR
- `/upload` - File Upload
- `/download_secret` - Sensitive Data Exposure
- `/redirect?next=...` - Open Redirect

## Warning
This app is intentionally insecure. Use only in isolated, controlled environments for security testing..
