#!/bin/sh

set -o errexit

python manage.py makemigrations
python manage.py migrate

gunicorn helm_bookstore.wsgi:application --bind 0.0.0.0:8000

exec "$@"
