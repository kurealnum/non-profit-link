# Setup

If you have any trouble setting up the project, contact me at with my contact information in README.md.

## Dependencies

- Python 3.12 >
- Docker

## Setup

- Initialize a virtual enviroment (venv) with `python3 -m venv env`.

- Once your venv is created and running, run `pip install -r requirements.txt`. Yes, we are running everything inside docker. However, I suggest you run a venv for your language servers (intellisense, basically).

- Having issues with psycopg2? You can simply choose to install `psycopg2-binary`. If this doesn't satisfy you, there are other solutions.

- Create a `.env` file in the root of the project

Here's what `.env` should contain (customize as you wish):

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
CORS_ALLOWED_ORIGINS='["http://localhost:8000"]'
```

- When you're ready to go, run `docker compose up`. Both PostgreSQL and Django are handled by Docker, so you don't really need to do anything. Once docker finishes building and launching, go to `localhost:8000` to access your project.
