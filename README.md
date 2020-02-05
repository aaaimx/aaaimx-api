# AAAIMX ADMIN Dashboard built with Django-admin & Django-Jet

## Setup
``` bash
$ pip install pipenv
$ pipenv install --python=python3 # Python 3.6 needed
```

## Local Settings
Create a local file `settings_local.py` to overwrite settings vars for development purposes:
```py
ALLOWED_HOSTS = ['*']
DEBUG=True
```

## Environment
`.env` File
```
export SECRET_KEY='SECRETO'
export DB_URI='postgres://USER:PASSWORD@HOST:PORT/DB_NAME'
```

## Docker PostgreSQL
    $  docker run -d -p 5432:5432 --name pg-aaaimx-admin -u postgres -e POSTGRES_PASSWORD=postgres postgres

## Run project

```bash
$ source .env
$ pipenv shell
$ python manage.py makemigrations # if database has changes
$ python manage.py migrate
$ python manage.py collectstatic
$ python manage.py runserver
```

## Setup database

### Generate backup
If `aaaimx-admin.json` not exists contact a administrator
```bash
$ python manage.py dumpdata --all -e authtoken -e admin -e dashboard -e sessions --natural-primary --indent=4 > aaaimx-admin.json
```

### If backup exists syncdb
```bash
$ python manage.py migrate --run-syncdb
$ python manage.py sqlflush
$ python manage.py loaddata aaaimx-admin.json
```

### Generate data from espcific app
```bash
$ python manage.py dumpdata finances --natural-primary --indent=4 > aaaimx-finances.json
```

Then restart project
```bash
$ python manage.py runserver
```