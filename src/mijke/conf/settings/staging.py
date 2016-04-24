import os
from .base import *

#
# Standard Django settings.
#

DEBUG = False
WSGI_APPLICATION = 'mijke.wsgi.wsgi.application'
ENVIRONMENT = 'staging'

ADMINS = (
    ('Sergei Maertens', 'info@regex-it.nl'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': 'localhost',
    }
}

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = [
    'localhost',
    'mijke.regex-it.nl',
]

LOGGING['loggers'].update({
    'django': {
        'handlers': ['django'],
        'level': 'WARNING',
        'propagate': True,
    },
})
