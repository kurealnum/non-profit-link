from flask import redirect, session
from functools import wraps

def login_required(f):
    """
    Decorate routes to require login.
    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def allowed_emails(email):
    #weird code, but it returns the name of the email. ex. bo_b@gmail.com returns gmail
    #not used yet, but it will be. I may have forgotten that I don't yet require an email 
    return email.rsplit('@', 1)[1].split('.',-1)[0]