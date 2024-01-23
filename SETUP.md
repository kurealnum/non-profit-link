# Setup

If you have any trouble setting up the project, contact me at with my contact information in README.md.

Make sure you have Python 3.x installed. Also, I'm assuming that you're working out of Windows PowerShell. If you aren't, the following commands might be a little bit different.

If you're working out of Windows CMD instead, the commands should _barely_ be different.

## Python Setup

- Initialize a virtual enviroment (venv) with `python3 -m venv env`. If you're using PowerShell _and_ you name your venv "env", you can use `./eact.ps1` to start your env. If you aren't using PowerShell, then read about venvs [here](https://docs.python.org/3/library/venv.html)

- Once your venv is created and running, run `pip install -r requirements.txt`

- Having issues with psycopg2? You can simply choose to install `psycopg2-binary`. If this doesn't satisfy you, there are other solutions.

- Double check to make sure you're ready to go by running `python manage.py runserver`. If this doesn't work, retrace your steps, and find out where you went wrong.

- If you'd like to create a superuser, just run `python manage.py createsuperuser`.

## Database Setup

We're using PostgreSQL (pronounced po-st-gree-skewl)! I'm not going to bother walking you through your database setup, as there's a lot of different ways that you can do it. All you need to do is:

- Create a "db_info.env" file in the `project/` folder, and create two fields like so: DB_PASSWORD="password_here" and DB_PORT=portnumberhere

- Update any required information in the Database section of settings.py.

- However you are going about your database setup, make sure that you have the `pg_trgm` module/extension installed to **both your main database and the template1 database.**
