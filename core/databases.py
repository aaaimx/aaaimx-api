# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
import os
import dj_database_url

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql'
    }
}

URL = os.environ.get('DATABASE_URL', None)
DATABASES['default'] = dj_database_url.config(default=URL, conn_max_age=0)
