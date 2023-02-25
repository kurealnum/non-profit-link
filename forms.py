from flask import render_template, request, redirect, url_for
import datetime

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

def search_home_page():
    if request.method == "GET":
        #USE request.ARGS for get requests, and requests.FORM for post requets
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
