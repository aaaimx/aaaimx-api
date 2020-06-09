#!/bin/sh

python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py sqlflush # clean db
python manage.py loaddata aaaimx-admin.json

exec "$@"