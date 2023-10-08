#!/bin/sh

set -o errexit

python manage.py makemigrations
python manage.py migrate
python manage.py test

gunicorn -b 0.0.0.0:8000 --access-logfile - --workers 3 --threads 3 --log-level=debug helm_bookstore.wsgi:application

exec "$@"
