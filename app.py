#dont bother importing all of flask, just import it as you need it
#python -m flask run :D
from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

from helpers import login_required


#loading env variables stuff, apparently you need the os module aswell
import os
from dotenv import load_dotenv
load_dotenv('paths_and_vars.env')

#db file is under .gitignore
import sqlite3

#connecting to the database
conn = sqlite3.connect(os.getenv('DATA_BASE_PATH'), check_same_thread=False)

with open('database\schema.sql') as f:
    conn.executescript(f.read())   


#some basic info to give flask
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


#Start of Login/Register-------------------


#TODO: the database isn't currently set up properly, I still need to modify the database and get the register page made
@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            flash("No username")
            return render_template('login.html')

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("No password")
            return render_template('login.html')

        # Query database for username
        rows = conn.execute("SELECT * FROM basic_users WHERE username = ?", (request.form.get("username"),))
        rows = rows.fetchall()

        # Ensure username exists and password is correct
        if len(rows) < 1 or not check_password_hash(rows[0][2], request.form.get("password")):
            flash("Wrong username/password")
            return render_template('login.html')

        # Remember which user has logged in
        session["user_id"] = rows[0][0]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


#TODO: the database isn't currently set up properly ^^
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation_password = request.form.get("confirmation")

        # Ensure username was submitted
        if not username:
            print("No username")
            return redirect("/register")

        # Ensure password was submitted
        elif not password:
            print("No password")
            return redirect("/register")
        #ensure confirmation password was submitted
        elif not confirmation_password:
            print("No  conf. password")
            return redirect("/register")

        #ensure username is original
        if username in conn.execute("SELECT username FROM basic_users"):
            print("Username is already in use")
            return redirect("/register")

        #ensure password matches confirmation password
        if confirmation_password != password:
            print("Password doesn't match confirmation password")
            return redirect("/register")

        # Put username into database
        conn.execute("INSERT INTO basic_users (username, password_hash) VALUES(?, ?)", (request.form.get("username"), generate_password_hash(request.form.get("password"))))
        conn.commit()

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")
    

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect(url_for("home"))


#End of Login/Register functions-------------------
#Start of main routes/functions-------------------


@app.route("/")
@login_required
def home():
    return render_template('index.html')


#methods go in a list to let flask and jinja2 know what methods we'll be using on this certain page
@app.route("/search", methods=["GET", "POST"])
@login_required
def home_search():

    #MAKE SURE TO RETURN THE FUNCTION THAT IS MADE IN FORMS!!!
    if request.method == "GET":
        #Use request.ARGS for get requests, and requests.FORM for post requets
        search = request.args.get("search_query")
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        conn.execute("INSERT INTO searches (search, time) VALUES (?,?)", (search, timestamp))
        conn.commit()

    if request.method == "POST":
        search = request.form.get("search_query")
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        conn.execute("INSERT INTO searches (search, time) VALUES (?,?)", (search, timestamp))
        conn.commit()
        return redirect(url_for('home'))
    
    return render_template('index.html', search_query=search)


@app.route("/about_us")
@login_required
def about_us():
    return render_template('aboutus.html')


@app.route("/technicals")
@login_required
def technicals():
    return render_template('technicals.html')


#End of main routes/functions-------------------
