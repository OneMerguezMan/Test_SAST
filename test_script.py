import sqlite3
import os
import subprocess
import requests
from flask import Flask, request, make_response

app = Flask(__name__)

# 1. Broken Access Control
@app.route('/admin')
def admin():
    # No authentication check
    return "Welcome, admin! (No access control)"

# 2. Cryptographic Failures
@app.route('/crypto')
def crypto():
    # Insecure: storing sensitive data in plaintext
    password = request.args.get('password', 'default')
    with open('passwords.txt', 'a') as f:
        f.write(password + '\n')
    return "Password stored insecurely!"

# 3. Injection
@app.route('/sql')
def sql():
    # Insecure: SQL Injection
    username = request.args.get('username', '')
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('CREATE TABLE users (username TEXT)')
    c.execute('INSERT INTO users VALUES ("admin")')
    query = f"SELECT * FROM users WHERE username = '{username}'"
    c.execute(query)
    result = c.fetchall()
    return str(result)

# 4. Insecure Design
@app.route('/insecure-design')
def insecure_design():
    # Insecure: No rate limiting, no validation
    return "No security design considered!"

# 5. Security Misconfiguration
@app.route('/misconfig')
def misconfig():
    # Insecure: Debug mode enabled
    app.debug = True
    return "Debug mode is ON!"

# 6. Vulnerable and Outdated Components
@app.route('/outdated')
def outdated():
    # Insecure: Using requests with known vulnerabilities (for demonstration)
    r = requests.get('http://example.com')
    return "Used potentially vulnerable library!"

# 7. Identification and Authentication Failures
@app.route('/auth')
def auth():
    # Insecure: Hardcoded credentials
    user = request.args.get('user', '')
    pwd = request.args.get('pwd', '')
    if user == 'admin' and pwd == 'password123':
        return "Authenticated!"
    return "Authentication failed!"

# 8. Software and Data Integrity Failures
@app.route('/integrity')
def integrity():
    # Insecure: Downloading and executing code from untrusted source
    url = request.args.get('url', '')
    if url:
        code = requests.get(url).text
        exec(code)  # Dangerous!
        return "Executed code from URL!"
    return "No URL provided."

# 9. Security Logging and Monitoring Failures
@app.route('/nolog')
def nolog():
    # Insecure: No logging of failed login attempts
    return "No logging implemented!"

# 10. Server-Side Request Forgery (SSRF)
@app.route('/ssrf')
def ssrf():
    # Insecure: Fetching user-supplied URL
    url = request.args.get('url', '')
    if url:
        r = requests.get(url)
        return r.text
    return "No URL provided."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 
