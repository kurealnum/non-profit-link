# NPL (Non Profit Link)

Written in Python, Django, React/JS, HTML, CSS, and SQLite3 (Postgres at some point)

**_Layout/Design:_** Look over [this](https://www.figma.com/file/pKaku2N7xVPbCGQb1p6LIJ/NPL?type=design&node-id=0-1&mode=design&t=mc7YWpRIbtvPRkHG-11) if you're trying to understand the project. However, everything will **_eventually be on .drawio files_**.

**_Some extra diagrams (might be unused):_** [Eraser.io](https://app.eraser.io/invite/CMPmi4yayzi3WI2kI1DS)

If you clone this project and create your own superuser, **_your email_** is your username on the Django Admin page.

# Setup

Make sure you have Python 3.10 and NPM installed. Also, I'm assuming that you're working out of Windows PowerShell. If you aren't, the following commands might be a little bit different.

## Python Setup

- Initialize a virtual enviroment (venv) with `python3 -m venv env`. If you're using PowerShell _and_ you name your venv "env", you can use `./eact.ps1` to start your env. If you aren't using PowerShell, then read about venvs [here](https://docs.python.org/3/library/venv.html)

- Once your venv is created and running, run `pip install -r requirements.txt`

- Double check to make sure you're ready to go by running `python manage.py runserver`. If this doesn't work, retrace your steps, and find out where you went wrong.

- If you'd like to create a superuser, just run `python manage.py createsuperuser`.

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

# Contact information

- Discord: **kureal#0464**
- Email: **oscar.gaske.cs@gmail.com**

# FAQ

## So... React?

Using React (and even JS) feels very overbearing and unnecessary for the current state of this project. That doesn't mean I won't use it in the future, but for now, I will be moving everything back to/writing everything in raw HTML/CSS, and I'll add in React when only when I _need_ it.

**Important:** the current files, components, etc. will all remain in this repository. I just won't be using them.

I've set up React so that you can use different files to control page renders. In other words, you can pick and choose which _compiled_ JS files you'd like to use.

Make sure to add your new TS/TSX files to `webpack.config.js`.

## What am I going to do with this/what is it for?

I will do my best to explain this, but no promises that it'll make sense. My mom frequently volunteers for local organizations such as food pantries and homeless shelters. These organizations might seem like they're always in need of every single supply, but that's not quite correct. In my own experience, I have observed that they often have an excess of some items but a shortage of others. The simple solution to this is just to share, but if there's not a platform to share/advertise these supplies on, that creates a problem since there's no communication between them, thus hindering them from sharing resources.

To resolve this, I'd like to develop a web application with Django that will enable these organizations to list what they have and what they need. There are a few other things that I want to do with this that I'll make note of over time, but for now, that's the main goal.

## What database will you/are you using?

SQLite. PostgreSQL (pronounced "post - gree - skew - l") in the future.
