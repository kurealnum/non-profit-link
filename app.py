#dont bother importing all of flask, just import it as you need it
from flask import Flask, render_template, request
from forms import search_home_page
#db file is under .gitignore
import sqlite3

#connecting to the database
conn = sqlite3.connect('database.db')

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


