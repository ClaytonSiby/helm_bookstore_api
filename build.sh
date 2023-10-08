#!/bin/sh

set -o errexit

python manage.py makemigrations
python manage.py migrate

gunicorn -b 0.0.0.0:8000 helm_bookstore.wsgi:application

exec "$@"
