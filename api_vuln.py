# api_vuln.py
from flask import Flask, request

app = Flask(__name__)

# Vulnérabilité : Pas d'authentification, endpoint exposé
@app.route('/delete_user', methods=['POST'])
def delete_user():
    username = request.form.get('username')
    # Vulnérabilité : Pas de vérification d'identité, suppression directe
    # (exemple d'Insecure Direct Object Reference - IDOR)
    return f"User {username} deleted!", 200

if __name__ == '__main__':
    app.run(debug=True) 
