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
            session['searchaddress'] = searchlist[0]
            session['searchcity'] = searchlist[1]
            session['searchdepart'] = searchlist[2]
            session['searcharrive'] = searchlist[3]
            session['searchzip'] = searchlist[4]
            session.modified = True
            return redirect("/list")
    else:
        if request.method == 'POST':
            flash('No orders found...')
    return render_template("sender.html")

@app.route('/traveler', methods=['GET', 'POST'])
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
        cursor.execute("INSERT INTO traveler (`destination`, `asking_price`, `departure_time`, `zipcode`, `arrival_time`, `user_index_user_id`,`fullname`) VALUES (%s, %s, %s, %s, %s, %s,%s)",\
            (requestlist[0],requestlist[1],requestlist[2],requestlist[3],requestlist[4], session['id'],session['name'],))
        mysql.connection.commit()
        flash("Itinerary posted.")
    return render_template("traveler.html")
    
@app.route('/list', methods=['GET', 'POST'])
def list():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM `traveler` INNER JOIN `user_index` WHERE `zipcode` = %s AND traveler.departure_time >= %s\
         AND traveler.arrival_time <= %s AND traveler.user_index_user_id = user_index.user_id AND user_index.user_id !=  %s", (session['searchzip'], session['searchdepart'], session['searcharrive'],session['id']))
    orders = cursor.fetchall()
    mysql.connection.commit()
    if request.method == 'POST' and 'requesttraveler' in request.form:
        cursor.execute("SELECT * FROM requests WHERE traveler_travelerindex1 = %s AND sender_id = %s AND request_id = %s", (request.form['requesttraveler'],session['id'],request.form['request_id']))
        chkrequest = cursor.fetchone()
        if chkrequest:
            flash('Already requested...')
        else:
            cursor.execute("INSERT INTO requests (`address_destination`, `city_destination`, `arrival_time`, `departure_time`, `zipcode`,\
                    `sender_id`, `request_id`, `requestfor`,`requestby`,`traveler_travelerindex1`, `acceptstatus`)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",\
                    (session['searchaddress'],session['searchcity'],request.form['arrival_time'],request.form['departure_time'],session['searchzip'], session['id'],\
                    request.form['request_id'], request.form['request_name'], session['name'], request.form['requesttraveler'],'0'))
            mysql.connection.commit()
            cursor.execute("SELECT * FROM `traveler` INNER JOIN `user_index` WHERE `zipcode` = %s AND traveler.departure_time >= %s\
            AND traveler.arrival_time <= %s AND traveler.user_index_user_id = user_index.user_id ", (session['searchzip'], session['searchdepart'], session['searcharrive'],))
            orders = cursor.fetchall()
            flash('Delivery requested...')      
    return render_template("list.html", orders=orders)

@app.route('/messagelist', methods=['GET', 'POST'])
def messagelist():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM `requests` WHERE `acceptstatus` = 1 AND (`request_id` = %s OR `sender_id` = %s)", (session['id'],session['id']))
    msglist = cursor.fetchall()
    if request.method == 'POST' and 'message' in request.form:
        session['currentmsg'] = request.form['message']
        session['sender_name'] = request.form['sendername']
        session['traveler_name'] = request.form['travelername']
        session['senderid'] = request.form['sender_id']
        session['travelerid'] = request.form['request_id']
        session.modified = True
        return redirect('/messageuser')
    return render_template("messagelist.html", msglist=msglist)

@app.route('/messageuser', methods=['GET', 'POST'])
def messageuser():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM `messages` WHERE  `traveler_travelerindex` = %s AND (`messenger_name` = %s OR `recipient_name` = %s)\
         AND (`messenger_name` = %s OR `recipient_name` = %s) ORDER BY `message_index` ASC ',(session['currentmsg'],session['name'],session['name'],session['sender_name'],session['sender_name']))
    convo = cursor.fetchall()
    cursor.execute('SELECT * FROM `messages` WHERE  `traveler_travelerindex` = %s AND (`messenger_name` = %s OR `recipient_name` = %s)\
         AND (`messenger_name` = %s OR `recipient_name` = %s) ORDER BY `message_index` ASC ',(session['currentmsg'],session['name'],session['name'],session['sender_name'],session['sender_name']))
    msgval = cursor.fetchone()
    if request.method == 'POST' and 'message' in request.form:
        cursor.execute("INSERT INTO `messages` (`messenger`, `messenger_name`,`recipient_name`,`message`,`traveler_travelerindex`)\
            VALUES (%s, %s, %s, %s, %s)",(session['id'],session['name'],request.form['recipient_name'],request.form['message'],request.form['travindex'],))
        cursor.execute('SELECT * FROM `messages` WHERE  `traveler_travelerindex` = %s AND (`messenger_name` = %s OR `recipient_name` = %s)\
         AND (`messenger_name` = %s OR `recipient_name` = %s) ORDER BY `message_index` ASC ',(session['currentmsg'],session['name'],session['name'],session['sender_name'],session['sender_name']))
        convo = cursor.fetchall()
        mysql.connection.commit()
    return render_template("messageuser.html", convo=convo, msgval=msgval)

@app.route('/requests', methods=['GET', 'POST'])
def requests():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM `requests` INNER JOIN `user_index` WHERE `request_id` = %s AND sender_id = user_index.user_id', (session['id'],))
    testlist = cursor.fetchall()
    if request.method == 'POST' and 'accept' in request.form:
        acceptmessage = "Request has been accepted."
        status = request.form['accept']
        cursor.execute("UPDATE requests SET acceptstatus = %s WHERE traveler_travelerindex1 = %s AND sender_id = %s AND request_id = %s",(1, status, request.form['sender_id'],session['id']))
        cursor.execute("INSERT INTO `messages` (`messenger`, `messenger_name`,`recipient_name`,`message`,`traveler_travelerindex`)\
            VALUES (%s, %s, %s, %s, %s)",(session['id'],session['name'],request.form['sender_name'],acceptmessage,status,))
        mysql.connection.commit()
        cursor.execute('SELECT * FROM `requests` INNER JOIN `user_index` WHERE `request_id` = %s AND sender_id = user_index.user_id', (session['id'],))
        testlist = cursor.fetchall()
        return redirect('/requests')
    elif request.method == 'POST' and 'reject' in request.form:
        status = request.form['reject']
        rejectsenderid = request.form['sender_id']
        cursor.execute("DELETE FROM requests WHERE `traveler_travelerindex1` = %s AND `acceptstatus` = 0 AND `request_id` = %s AND `sender_id` = %s",(status,session['id'],rejectsenderid))
        mysql.connection.commit()
        cursor.execute('SELECT * FROM `requests` INNER JOIN `user_index` WHERE `request_id` = %s AND sender_id = user_index.user_id', (session['id'],))
        testlist = cursor.fetchall()
        return redirect('/requests')
    return render_template("requests.html", testlist=testlist)
    
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST' and 'user' in request.form and 'password' in request.form:
        user = request.form['user']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM user_index WHERE `email address`= %s AND password = %s", (user, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['user_id']
            session['name'] = account['firstname'] + ' ' +account['lastname']
            session['user'] = account['email address']
            return redirect("http://127.0.0.1:5000")
        else:
            flash('Incorrect username/password!')
    elif request.method == 'POST' and 'email' in request.form and 'password' in request.form and 'firstname' in request.form and 'lastname' in request.form and 'phone' in request.form:
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
            return redirect('/signin')
    elif request.method == 'POST':
        flash("Nothing inputted!")
    return render_template("signin.html")

@app.route('/logout')
def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   session.pop('searchzip', None)
   session.pop('searchdepart', None)
   session.pop('searcharrive', None)
   session.pop('currentmsg', None)
   session.pop('name', None)
   session.pop('sender_name', None)
   session.pop('traveler_name', None)
   session.pop('senderid', None)
   session.pop('travelerid', None)
   return redirect("http://127.0.0.1:5000")
    
    