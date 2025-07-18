from flask import Flask, request, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'supersecretkey123'  # Hardcoded secret key

def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL Injection vulnerability
    query = "SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password)
    cursor.execute(query)
    user = cursor.fetchone()

    if user:
        session['user_id'] = user[0]
        return "Logged in successfully"
    else:
        return "Invalid credentials"

