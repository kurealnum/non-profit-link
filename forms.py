from flask import Flask, render_template, request
import time

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

def return_time():
    t = time.localtime()
    return time.strftime("%H:%M:%S", t)


def search_home_page():
    if request.method == "POST":
        search = request.form.get("search_query")
        conn.execute("INSERT INTO searches (search, time) VALUES (?,?)", (search, return_time()))
        conn.commit()

    return render_template('index.html', search_query=search)
