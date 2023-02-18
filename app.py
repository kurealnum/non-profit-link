#dont bother importing all of flask, just import it as you need it
from flask import Flask, render_template, request

#some basic info to give flask
app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/search_home_page", methods=["POST", "GET"])
def search_home_page():
    if request.method == "POST":
        search = request.form.get("search_query")

    return render_template('index.html', search_query=search)


