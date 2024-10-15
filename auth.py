import string
import random
import mysql.connector
from flask import Blueprint, render_template, request, redirect, url_for



auth = Blueprint('auth', __name__)

# MySQL configurations
db_config = {
    'user': 'mysql',
    'password': 'MCAmca2024-*',
    'host': 'localhost',
    'database': 'crop24'
}

# Database connection function
def get_db_connection():
    return mysql.connector.connect(**db_config)
users = {}

def generate_captcha():
    letters = string.ascii_letters
    captcha = ''.join(random.choice(letters) for i in range(6))
    return captcha

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        email_id = request.form['email_id']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']

        if password != confirm_password:
            message = 'Passwords do not match!'
            return render_template('signup.html', message=message)
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM login WHERE username = %s', (username,))
        account = cursor.fetchone()
        
        if account:
            message = 'Account already exists!'
        else:
            cursor.execute('INSERT INTO login (username, email_id, password) VALUES (%s, %s, %s)', (username, email_id, password))
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(('login'))
        
        cursor.close()
        conn.close()
    return render_template('signup.html', message=message)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM login WHERE username = %s AND password = %s', (username, password))
        account = cursor.fetchone()
        
        if account:
            message = 'Login successful!'
            return redirect(('home'))
        else:
            message = 'Invalid username or password!'
        
        cursor.close()
        conn.close()
    return render_template('login.html', message=message)

@auth.route('/')
def home():
    return render_template('index.html')

