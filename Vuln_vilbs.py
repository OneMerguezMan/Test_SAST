#!/usr/bin/env python3
"""
Demo script with vulnerable dependencies
For educational purposes only
"""

import requests
import yaml
import flask
import django
import cryptography
import pillow
import numpy
import tensorflow
import sqlalchemy
from xml.etree.ElementTree import parse

def insecure_deserialization():
    """Demo of unsafe YAML deserialization"""
    dangerous_yaml = """
    !!python/object/apply:os.system
    args: ['echo "This could be dangerous"']
    """
    try:
        yaml.load(dangerous_yaml)  # Unsafe, should use yaml.safe_load()
    except:
        print("[!] YAML execution blocked")

def insecure_request():
    """Demo of insecure request with SSL verification disabled"""
    try:
        response = requests.get(
            'https://example.com',
            verify=False  # Désactive la vérification SSL
        )
    except:
        print("[!] Request failed")

def sql_injection_vulnerable():
    """Demo of SQL injection vulnerability"""
    from sqlalchemy import create_engine, text
    
    engine = create_engine('sqlite:///:memory:')
    user_input = "admin' --"
    
    # Vulnérable à l'injection SQL
    query = text(f"SELECT * FROM users WHERE username = '{user_input}'")
    
    try:
        with engine.connect() as conn:
            result = conn.execute(query)
    except:
        print("[!] SQL query failed")

def main():
    print("Testing vulnerable dependencies...")
    insecure_deserialization()
    insecure_request()
    sql_injection_vulnerable()

if __name__ == "__main__":
    main() 
