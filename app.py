from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.secret_key = '12345wasdf'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mydb'

mysql = MySQL(app)



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sender')
def sender():
    return render_template("sender.html")

@app.route('/carrier')
def carrier():
    return render_template("carrier.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")
    
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    msg = 'test'
    if request.method == 'POST' and 'user' in request.form and 'password' in request.form:
        user = request.form['user']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user_index WHERE username= %s AND password = %s', (user, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            # session['id'] = account['id']
            session['username'] = account['username']
            return redirect("http://127.0.0.1:5000")
        else:
            msg = 'Incorrect username/password!'
    return render_template("signin.html")

@app.route('/logout')
def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   return redirect("http://127.0.0.1:5000")
    
    
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form and 'firstname' in request.form and 'lastname' in request.form and 'phone' in request.form:
        email = request.form['email']
        password = request.form['password']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        phone = request.form['phone']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM user_index WHERE `email address` = %s", [email])
        account = cursor.fetchone()
        if account:
            flash("Account already exists!")
        elif not email or not password or not firstname or not lastname or not phone:
            flash("No information inputted...")
        else:
            cursor.execute("INSERT INTO user_index VALUES(%s, %s, %s, %s, %s)", (email, password, firstname, lastname, phone))
            mysql.connection.commit()
            flash("Registered successfully!")
    elif request.method == 'POST':
        flash("Nothing inputted!")
    return render_template("signup.html")
    
    