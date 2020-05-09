# AAAIMX API

## Environment
`.env` File
```
export SECRET_KEY='SECRETO'
export DB_URI='postgres://USER:PASSWORD@HOST:PORT/DB_NAME'
```

## Docker PostgreSQL
    $ docker run -d -p 5432:5432 --name pg-aaaimx-admin -u postgres -e POSTGRES_PASSWORD=postgres postgres

## Run project

```bash
$ source .env
$ source venv/bin/activate
$ chmod +x bin/enstrypoint.sh
$ python manage.py createuseruser
```

### Google Drive Storage

## Setup database

### Generate backup
If `aaaimx-admin.json` not exists contact a administrator
```bash
$ python manage.py dumpdata --all -e authtoken -e admin -e dashboard -e sessions --natural-primary --indent=4 > aaaimx-admin.json
```

### If backup exists syncdb
```bash
$ python manage.py migrate --run-syncdb
$ python manage.py sqlflush # clean db
$ python manage.py loaddata aaaimx-admin.json
```

### Generate data from especific app
```bash
$ python manage.py dumpdata finances --natural-primary --indent=4 > aaaimx-finances.json
```

Then start project
```bash
$ python manage.py runserver
```

Open browser in http://localhost:8000
Open browser in http://localhost:8000/api