from flask import redirect, session, flash, render_template
from functools import wraps

"""
Decorate routes to require login.
https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
"""
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

'''
weird code, but it returns the name of the email. ex. bo_b@gmail.com returns gmail
not used yet, but it will be. I may have forgotten that I don't yet require an email
''' 
def allowed_emails(email):
    return email.rsplit('@', 1)[1].split('.',-1)[0]

def flash_render(msg, template):
    flash(msg)
    return render_template(template)
