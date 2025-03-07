# Setup

If you have any trouble setting up the project, contact me at with my contact information in README.md.

Make sure you have Python 3.x installed. Also, I'm assuming that you're working out of Windows PowerShell. If you aren't, the following commands might be a little bit different.

If you're working out of Windows CMD instead, the commands should _barely_ be different.

## Python Setup

- Initialize a virtual enviroment (venv) with `python3 -m venv env`.

- Once your venv is created and running, run `pip install -r requirements.txt`

- Having issues with psycopg2? You can simply choose to install `psycopg2-binary`. If this doesn't satisfy you, there are other solutions.

- Double check to make sure you're ready to go by running `python3 manage.py runserver`. If this doesn't work, retrace your steps, and find out where you went wrong.

- If you'd like to create a superuser, just run `python manage.py createsuperuser`.

## Database Setup

We're using PostgreSQL (pronounced po-st-gree-skewl)! I'm not going to bother walking you through your database setup, as there's a lot of different ways that you can do it. All you need to do is:

- Create a "secrets.env" file in the `project/` folder

Here's what `db_info.env` should contain:

```
DB_PASSWORD="testtest"
DB_PORT=5432
DB_USERNAME="oscar"

DJANGO_SECRET_KEY="mysecretkey"
DEBUG=True
ALLOWED_HOSTS='["localhost", "127.0.0.1"]'
CSRF_COOKIE_SECURE=False
SESSION_COOKIE_SECURE=False
SECURE_SSL_REDIRECT=False
SECURE_HSTS_SECONDS=0
SECURE_HSTS_INCLUDE_SUBDOMAINS=False
SECURE_HSTS_PRELOAD=False
```

- Update any required information in the Database section of settings.py.

- However you are going about your database setup, make sure that you have the `pg_trgm` module/extension installed to **both your main database and the template1 database.**

If you have any questions, please feel free to contact me through any of the methods listed in the README.
