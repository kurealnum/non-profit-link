from flask import Flask, render_template, request

def search_home_page():
    if request.method == "POST":
        search = request.form.get("search_query")

    return render_template('index.html', search_query=search)
