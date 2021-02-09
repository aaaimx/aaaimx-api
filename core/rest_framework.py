import os
import datetime

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly",
        # 'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.IsAdminUser'
    ],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend",
                                "rest_framework.filters.OrderingFilter",
                                "rest_framework.filters.SearchFilter", ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        # "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(hours=1),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(days=1),
    "USER_ID_FIELD": "username",
    'USER_ID_CLAIM': 'username',
    'UPDATE_LAST_LOGIN': True,
}

# Django Cors Headers
# https://pypi.org/project/django-cors-headers/

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = os.environ.get("DJANGO_ALLOWED_ORIGINS").split(' ')
