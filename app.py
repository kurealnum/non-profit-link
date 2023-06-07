#dont bother importing all of flask, just import it as you need it
#python -m flask run :D
from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

from helpers import login_required, flash_render


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


@app.route("/login", methods=["GET", "POST"])
def login():

    #clear the session
    session.clear()

    #variables 
    username = request.form.get("username")
    password = request.form.get("password")

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not username:
            return flash_render("No username", "login.html")

        # Ensure password was submitted
        elif not password:
            return flash_render("No password", "login.html")

        # Query database for username
        rows = conn.execute("SELECT * FROM basic_users WHERE username = ?", (username,))
        rows = rows.fetchall()

        # Ensure username exists and password is correct
        if len(rows) < 1 or not check_password_hash(rows[0][2], password):
            flash_render("Wrong username/password", "login.html")

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
            return flash_render("No username", "register.html")

        # Ensure password was submitted
        elif not password:
            return flash_render("No password", "register.html")
        
        #ensure confirmation password was submitted
        elif not confirmation_password:
            return flash_render("No conf. password", "register.html")

        #ensure username is original
        if username in conn.execute("SELECT username FROM basic_users"):
            return flash_render("Username is already in use", "register.html")

        #ensure password matches confirmation password
        if confirmation_password != password:
            return flash_render("Password doesn't match confirmation password", "register.html")
        
        #ensure the password is longer than 8 characters
        if len(password) < 8:
            return flash_render("Password needs to be 8 characters or longer", "register.html")

        # Put username into database
        conn.execute("INSERT INTO basic_users (username, password_hash, user_type) VALUES(?, ?, ?)", (username, generate_password_hash(password), "basic"))
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
def search():

    if request.method == "GET":
        #Use request.ARGS for get requests, and requests.FORM for post requests
        pass

    elif request.method == "POST":
        #variables
        user_id = session["user_id"]
        #storing the search query (and the time)
        search = request.form["search"]
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
         
        #saving the value of the search
        conn.execute("INSERT INTO searches (user_id, search) VALUES (?, ?)", (user_id, search))

        #saving the time of the search
        conn.execute("INSERT INTO searches_time (user_id, time_stamp) VALUES (?, ?)", (user_id,timestamp))
        conn.commit()

        if search == "":
            org_rows = None

        else:
            sql_statement = ("SELECT orgs_loc.org_name, country, region, zip, city, street_address, website "
                             "FROM orgs_loc "
                             "JOIN orgs_info ON orgs_info.org_id = orgs_loc.org_id "
                             "WHERE SUBSTR(zip,1,?) = ?")
            
            org_returns = conn.execute(sql_statement, (len(search), search))
            #theres no way to check the length of this object, so we instead check if fetchall() has anything in it
            org_rows = org_returns.fetchall()

            if len(org_rows) < 1:
                org_rows = False
                
        #this is whats returned when the fetch function in searchhelper.js is called
        return render_template('searched.html', items=org_rows, websites=None)
    
    return render_template('search.html')


@app.route("/about_us")
@login_required
def about_us():
    return render_template('aboutus.html')


@app.route("/technicals")
@login_required
def technicals():
    return render_template('technicals.html')


#End of main routes/functions-------------------
