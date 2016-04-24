from pathlib import Path

import django.conf.global_settings as DEFAULT_SETTINGS
from django.contrib.messages import constants as message_constants
from django.utils.translation import ugettext_lazy as _

# Automatically figure out the ROOT_DIR and PROJECT_DIR.
path = Path(__file__)
DJANGO_PROJECT_DIR = path.parent.parent.parent
ROOT_DIR = DJANGO_PROJECT_DIR.parent.parent

#
# Standard Django settings.
#

DEBUG = False

SITE_ID = 1
PROJECT_NAME = 'mijke'

ADMINS = (
    ('Admin', 'sergeimaertens@xbbtx.be'),
)
MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = 'noreply@xbbtx.be'

# Hosts/domain names that are valid for this site; required if DEBUG is False
# https://docs.djangoproject.com/en/1.7/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
TIME_ZONE = 'Europe/Brussels'

LOCALE_PATHS = (
    str(DJANGO_PROJECT_DIR / 'conf' / 'locale'),
)

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('nl', _('Dutch')),
)
LANGUAGE_CODE = 'nl'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = str(ROOT_DIR / 'static')

STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    str(DJANGO_PROJECT_DIR / 'static'),
    str(DJANGO_PROJECT_DIR / 'node_modules' / 'normalize.css'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
]

MEDIA_ROOT = str(ROOT_DIR / 'media')

MEDIA_URL = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'jl+pq@4%ds89h8hihx4-&1^b-d!wvx*@l-7fj0b48bkq2*d3di'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            str(DJANGO_PROJECT_DIR / 'templates'),
        ],
        'OPTIONS': {
            'context_processors': DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
                'django.template.context_processors.request',
                'mijke.utils.context_processors.settings',
            )
        }
    },
]

MIDDLEWARE_CLASSES = [
    # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # External middleware.
    'axes.middleware.FailedLoginMiddleware',

    # CMS
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'mijke.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'mijke.wsgi.application'

INSTALLED_APPS = [

    # Note: contenttypes should be first, see Django ticket #10827
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Optional applications.
    'django.contrib.admin',

    # External applications.
    'axes',
    'compressor',
    'rest_framework',
    'sniplates',

    # CMS
    'taggit',
    'modelcluster',

    'wagtail.wagtailcore',
    'wagtail.wagtailadmin',
    'wagtail.wagtaildocs',
    'wagtail.wagtailsnippets',
    'wagtail.wagtailusers',
    'wagtail.wagtailimages',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsearch',
    'wagtail.wagtailsites',
    'wagtail.wagtailredirects',
    'wagtail.wagtailforms',

    # Project applications.
    'mijke.albums',
]

LOGGING_DIR = ROOT_DIR / 'log'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(name)s %(module)s %(process)d %(thread)d  %(message)s'
        },
        'timestamped': {
            'format': '%(asctime)s %(levelname)s %(name)s  %(message)s'
        },
        'simple': {
            'format': '%(levelname)s  %(message)s'
        },
        'performance': {
            'format': '%(asctime)s %(process)d | %(thread)d | %(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'timestamped'
        },
        'django': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(LOGGING_DIR / 'django.log'),
            'formatter': 'verbose',
            'maxBytes': 1024*1024*10,  # 10 MB
            'backupCount': 10
        },
        'project': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(LOGGING_DIR / 'mijke.log'),
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 10
        },
        'performance': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(LOGGING_DIR / 'performance.log'),
            'formatter': 'performance',
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 10
        },
    },
    'loggers': {
        'mijke': {
            'handlers': ['project'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#
# Additional Django settings
# Enable these when using HTTPS
#

# SESSION_COOKIE_SECURE = True
# SESSION_COOKIE_HTTPONLY = True
# CSRF_COOKIE_SECURE = True
# X_FRAME_OPTIONS = 'DENY'

MESSAGE_TAGS = {
    message_constants.DEBUG: 'debug',
    message_constants.INFO: 'info',
    message_constants.SUCCESS: 'success',
    message_constants.WARNING: 'warning',
    message_constants.ERROR: 'danger'
}

TEST_RUNNER = 'django.test.runner.DiscoverRunner'
ENVIRONMENT = None
SHOW_ALERT = True

#
# Django-axes
#
AXES_LOGIN_FAILURE_LIMIT = 30  # Default: 3
AXES_LOCK_OUT_AT_FAILURE = True  # Default: True
AXES_USE_USER_AGENT = False  # Default: False
AXES_COOLOFF_TIME = 1  # One hour


#
# Wagtail
#
WAGTAIL_SITE_NAME = 'Mijke Fotografie'

#
# Compressor
#
COMPRESS_PRECOMPILERS = ()
