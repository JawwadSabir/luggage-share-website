from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_mysqldb import MySQL
from datetime import datetime
import MySQLdb.cursors
import re

app = Flask(__name__)

app.secret_key = '12345wasdf'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mydb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


@app.route('/')
def index():
   return render_template("index.html")

@app.route('/sender', methods=['GET', 'POST'])
def sender():
    if request.method == 'POST' and 'address' in request.form and 'citydestination' in request.form\
        and 'departuresender' in request.form and 'arrivalsender' in request.form and 'zipsender' in request.form:
            searchlist = []
            searchlist.append(request.form['address']) 
            searchlist.append(request.form['citydestination'])
            searchlist.append(datetime.strptime(request.form['departuresender'],'%m/%d/%Y').strftime('%Y-%m-%d'))
            searchlist.append(datetime.strptime(request.form['arrivalsender'],'%m/%d/%Y').strftime('%Y-%m-%d'))
            searchlist.append(request.form['zipsender'])
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM traveler WHERE zipcode = %s", (searchlist[4],))
            orders = cursor.fetchone()
            if orders:
                cursor.execute("INSERT INTO sender VALUES (%s, %s, %s, %s, %s, %s)",\
                    (searchlist[0],searchlist[1],searchlist[2],searchlist[3],searchlist[4],session['id']))
                mysql.connection.commit()
                session['searchzip'] = orders['zipcode']
                session.modified = True
                return redirect("/list")
            else:
                flash('No orders found...')
    return render_template("sender.html")

@app.route('/carrier', methods=['GET', 'POST'])
def carrier():
    if request.method == 'POST' and 'departuretraveler' in request.form\
        and 'destinationtraveler' in request.form and 'arrivaltraveler' in request.form and 'asktraveler' in request.form\
        and 'ziptraveler' in request.form:
        requestlist = []
        requestlist.append(request.form['destinationtraveler'])
        requestlist.append(request.form['asktraveler'])
        requestlist.append(datetime.strptime(request.form['departuretraveler'],'%m/%d/%Y').strftime('%Y-%m-%d'))
        requestlist.append(request.form['ziptraveler'])
        requestlist.append(datetime.strptime(request.form['arrivaltraveler'],'%m/%d/%Y').strftime('%Y-%m-%d'))
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO traveler VALUES (%s, %s, %s, %s, %s, %s)",\
             (requestlist[0],requestlist[1],requestlist[2],requestlist[3],requestlist[4], session['id']))
        mysql.connection.commit()
    return render_template("carrier.html")
    
@app.route('/list', methods=['GET', 'POST'])
def list():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM traveler WHERE zipcode = %s", (session['searchzip'],))
    orders = cursor.fetchall()
    cursor.execute("SELECT * FROM user_index WHERE user_id = %s", (orders['user_index_user_id'],))
    hold = cursor.fetchall()
    mysql.connection.commit()
    if request.method == 'POST' and 'requesttraveler' in request.form:
        cursor.execute("SELECT user_index_user_id FROM traveler WHERE travelerindex = %s", (request.form['requesttraveler']))
        temp = cursor.fetchone()
        travid = temp['user_index_user_id']
        cursor.execute("SELECT * FROM sender WHERE user_index_user_id = %s", (session['id'],))
        senderrequest = cursor.fetchone()
        cursor.execute("INSERT INTO requests VALUES (%s, %s, %s, %s, %s, %s, %s)", (senderrequest['address_destination'],senderrequest['city_destination'],senderrequest['arrival_time'],\
            senderrequest['zipcode'], senderrequest['departure_time'],session['id'],travid))
        mysql.connection.commit()
        flash('Delivery requested...')
    return render_template("list.html", orders=orders)

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/requests')
def requests():
    return render_template("requests.html")
    
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST' and 'user' in request.form and 'password' in request.form:
        user = request.form['user']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user_index WHERE `email address`= %s AND password = %s', (user, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['user_id']
            session['user'] = account['email address']
            return redirect("http://127.0.0.1:5000")
        else:
            flash('Incorrect username/password!')
    return render_template("signin.html")

@app.route('/logout')
def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   session.pop('searchzip', None)
   return redirect("http://127.0.0.1:5000")
    
    
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form and 'firstname' in request.form and 'lastname' in request.form and 'phone' in request.form:
        email = request.form['email']
        password = request.form['password']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        phone = request.form['phone']
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM user_index WHERE `email address` = %s", [email])
        account = cursor.fetchone()
        if account:
            flash("Account already exists!")
        elif not email or not password or not firstname or not lastname or not phone:
            flash("All fields are not filled...")
        else:
            cursor.execute("INSERT INTO user_index VALUES(%s, %s, %s, %s, %s, NULL)", (email, password, firstname, lastname, phone))
            mysql.connection.commit()
            flash("Registered successfully!")
    elif request.method == 'POST':
        flash("Nothing inputted!")
    return render_template("signup.html")
    
    