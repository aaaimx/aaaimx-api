# AAAIMX ADMIN Dashboard built with Django-admin & Django-Jet



# MySQL Client
sudo apt-get install libmysqlclient-dev

# Setup
``` bash
$ pip install pipenv
$ pipenv install --python=python3
```

# Environment

`.env` File
```
export SECRET_KEY='SECRETO'
export DB_URI='postgres://USER:PASSWORD@HOST:PORT/DB_NAME'
```

# Docker 
```bash
$  docker run -d -p 33060:3306 --name mysql-db -e MYSQL_ROOT_PASSWORD=secret mysql --default-authentication-plugin=mysql_native_password
```

# Run project

```bash
$ source .env
$ pipenv shell
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py collectstatic
$ python manage.py runserver
```

## Dashboard

![](./ss.jpeg)


## Setup database

```bash
$ python manage.py dumpdata --all -e authtoken -e admin -e dashboard -e sessions --natural-primary --indent=4 > aaaimx-admin.json
```

```bash
$ python manage.py migrate --run-syncdb --database=postgres
$ python manage.py sqlflush --database=postgres
$ python manage.py loaddata aaaimx-admin.json --database=postgres
```

```bash
$ python manage.py dumpdata finances --natural-primary --indent=4 > aaaimx-finances.json
```