# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

URL = os.environ.get('DATABASE_URL', None)
DATABASES['default'] = dj_database_url.config(default=URL, conn_max_age=0)
