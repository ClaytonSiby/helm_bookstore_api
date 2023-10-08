#!/bin/sh

set -o errexit

python manage.py makemigrations
python manage.py migrate
python manage.py test

python manage.py runserver 0.0.0.0:8000

exec "$@"
