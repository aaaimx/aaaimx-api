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
export SECRET_KEY='YOUR SECRET KEY'
export DB_NAME='YOUR DATABASE NAME'
export DB_USER='YOUR DB USER'
export DB_PASS='YOUR DB PASSWORD'
export DB_HOST='YOUR DB HOST'
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