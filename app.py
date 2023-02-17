#dont bother importing all of flask, just import it as you need it
from flask import Flask, render_template, request

#some basic info to give flask
app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/")
def home():
    return render_template('index.html')

#methods go in a list to let flask and jinja2 know what methods we'll be using on this certain page
@app.route("/greet", methods=["POST", "GET"])
def greet():
    #name = getting the request form from the html
    name = request.form['name_input']
    #we then use index.html, and pass in name as name
    return render_template('index.html', name = name)