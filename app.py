#dont bother importing all of flask, just import it as you need it
from flask import Flask, render_template, request
from forms import search_home_page
#db file is under .gitignore
import sqlite3

#connecting to the database
conn = sqlite3.connect('database\database.db')

with open('database\schema.sql') as f:
    conn.executescript(f.read())   

#some basic info to give flask
app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/")
def home():
    return render_template('index.html')

#methods go in a list to let flask and jinja2 know what methods we'll be using on this certain page
@app.route("/search_home_page", methods=["POST", "GET"])
def home_search():
    #MAKE SURE TO RETURN THE FUNCTION THAT IS MADE IN FORMS!!!
    return search_home_page()

#just a test function, not planning on keeping it
def insert_search(term):
    conn.execute("INSERT INTO searches (search) VALUES (?)", (term,))
    #gonna find a better way to commit the databse, because this could
    #be slow on a larger scale
    conn.commit()

insert_search('Search')


