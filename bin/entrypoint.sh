#!/bin/sh

# python manage.py flush --no-input
# python manage.py makemigrations
python manage.py migrate
# python manage.py createsuperuser --user "${SU_NAME}"
python manage.py collectstatic --no-input

exec "$@"
