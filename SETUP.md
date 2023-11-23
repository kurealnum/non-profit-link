# Setup

Make sure you have Python 3.10 and NPM installed. Also, I'm assuming that you're working out of Windows PowerShell. If you aren't, the following commands might be a little bit different.

## Python Setup

- Initialize a virtual enviroment (venv) with `python3 -m venv env`. If you're using PowerShell _and_ you name your venv "env", you can use `./eact.ps1` to start your env. If you aren't using PowerShell, then read about venvs [here](https://docs.python.org/3/library/venv.html)

- Once your venv is created and running, run `pip install -r requirements.txt`

- Double check to make sure you're ready to go by running `python manage.py runserver`. If this doesn't work, retrace your steps, and find out where you went wrong.

- If you'd like to create a superuser, just run `python manage.py createsuperuser`.

## Database Setup

We're using PostgreSQL (pronounced po-st-gree-skewl)! I'm not going to bother walking you through your database setup, as there's a lot of different ways that you can do it. All you need to do is:

- Create a "db_password.env" file in the `project/` folder, and create a field like so: DB_PASSWORD="password_here"

- Update any required information in the Database section of settings.py.

## NPM/React/TypeScript Setup

I might lose some of you here, so try and stay with me. Making React work with Django is hard enough, but throwing TypeScript in just creates a whole different mess. I have a pretty good setup at the moment, but improvements are _always_ welcome.

Also, keep in mind that all of these commands should be run from the _root folder_ of the project

- Start by running `npm install`. This should install everything in package-lock.json.

- Then, attempt to run `npm run dev` (builds your project). Unless specified in the most recent commit, there should be no build issues.

Confused about which folders are which? Check out the [folders](#folders) section.

As long as these commands run, you should be good to go! Check out the [react](#so-react) section to start contributing!

## Folders

- **.vscode**: Just VSCode settings
- **apps**: All apps, future and present
- **assets**: All TS/TSX files, i.e. all raw files for React
- **diagrams**: Draw.io files. Just a database diagram at the moment
- **django_static**: Static that is only accessed by Django
- **project**: Project folder for Django
- **react_static**: All React stuff is compiled (well, technically transpiled) here. Django then takes the JS and any other files that it needs, if that makes any sense.
- **templates**: Templates for Django!
