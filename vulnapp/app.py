from flask import Flask, request, render_template_string, redirect, send_file, session, url_for
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Sensitive Data Exposure

# --- Database setup ---
def init_db():
    conn = sqlite3.connect('vulnapp.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, owner TEXT, content TEXT)')
    c.execute('INSERT OR IGNORE INTO users (id, username, password) VALUES (1, "admin", "admin123")')
    c.execute('INSERT OR IGNORE INTO notes (id, owner, content) VALUES (1, "admin", "This is a secret note.")')
    conn.commit()
    conn.close()

init_db()

# --- SQL Injection ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Vulnerable SQL query
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        conn = sqlite3.connect('vulnapp.db')
        c = conn.cursor()
        c.execute(query)
        user = c.fetchone()
        conn.close()
        if user:
            session['user'] = username
            return redirect('/dashboard')
        else:
            return 'Login failed!'
    return '''<form method="post">Username: <input name="username"><br>Password: <input name="password" type="password"><br><input type="submit"></form>'''

# --- XSS ---
@app.route('/greet')
def greet():
    name = request.args.get('name', '')
    # Vulnerable to reflected XSS
    return render_template_string(f'<h1>Hello, {name}!</h1>')

# --- Command Injection ---
@app.route('/ping', methods=['GET', 'POST'])
def ping():
    if request.method == 'POST':
        host = request.form['host']
        # Vulnerable to command injection
        output = os.popen(f'ping -c 1 {host}').read()
        return f'<pre>{output}</pre>'
    return '''<form method="post">Host: <input name="host"><input type="submit"></form>'''

# --- IDOR ---
@app.route('/note/<int:note_id>')
def note(note_id):
    # No access control: IDOR
    conn = sqlite3.connect('vulnapp.db')
    c = conn.cursor()
    c.execute('SELECT content FROM notes WHERE id=?', (note_id,))
    row = c.fetchone()
    conn.close()
    if row:
        return f'Note: {row[0]}'
    return 'Note not found.'

# --- File Upload Vulnerability ---
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        # No file type check, saves with original filename
        f.save(os.path.join('uploads', f.filename))
        return 'File uploaded!'
    return '''<form method="post" enctype="multipart/form-data">File: <input type="file" name="file"><input type="submit"></form>'''

# --- Sensitive Data Exposure ---
@app.route('/download_secret')
def download_secret():
    # Exposes a sensitive file
    return send_file('app.py')

# --- Open Redirect ---
@app.route('/redirect')
def open_redirect():
    target = request.args.get('next', '/')
    return redirect(target)

# --- Dashboard ---
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')
    return f'Welcome, {session["user"]}! <a href="/logout">Logout</a>'

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True, host='0.0.0.0', port=5000) 