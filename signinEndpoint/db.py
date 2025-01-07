from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_mysqldb import MySQL
from flask_session import Session
import MySQLdb.cursors
import re

app = Flask(__name__)

# Secret key for session management
app.secret_key = 'your_secret_key'

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
app.config['MYSQL_DB'] = 'your_database_name'

# Session configurations
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        account = cursor.fetchone()
        
        if account:
            flash('Account already exists!')
        elif not re.match(r'^[a-zA-Z0-9]+$', username):
            flash('Username must contain only characters and numbers!')
        elif not username or not password:
            flash('Please fill out the form!')
        else:
            cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
            mysql.connection.commit()
            flash('You have successfully registered!')
            return redirect(url_for('signin'))
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        account = cursor.fetchone()
        
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            flash('Logged in successfully!')
            return redirect(url_for('profile'))
        else:
            flash('Incorrect username/password!')
    return render_template('signin.html')

@app.route('/profile')
def profile():
    if 'loggedin' in session:
        return render_template('profile.html', username=session['username'])
    return redirect(url_for('signin'))

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    flash('You have successfully logged out!')
    return redirect(url_for('signin'))

if __name__ == '__main__':
    app.run(debug=True)