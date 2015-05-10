from .settings import *

#
# Standard Django settings.
#

DEBUG = True
TEMPLATE_DEBUG = DEBUG
WSGI_APPLICATION = 'mijke_fotografie.wsgi.wsgi_development.application'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ENVIRONMENT = 'development'

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ROOT_DIR, 'mijke_fotografie.db'),
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

LOGGING['loggers'].update({
    'mijke_fotografie': {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propagate': True,
    },
    'django': {
        'handlers': ['django'],
        'level': 'DEBUG',
        'propagate': True,
    },
    'performance': {
        'handlers': ['performance'],
        'level': 'INFO',
        'propagate': True,
    },
})

# Additional Django settings
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = False
CSRF_COOKIE_SECURE = False

#
# Django debug toolbar
#
INSTALLED_APPS += [
    'debug_toolbar',
]
MIDDLEWARE_CLASSES += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}

#
# Skip migrations in Django 1.7
#
def prevent_tests_migrate(db):
    import django
    from django.db import connections
    from django.db.migrations.executor import MigrationExecutor
    django.setup()
    ma = MigrationExecutor(connections[db]).loader.migrated_apps
    return dict(zip(ma, ['{a}.notmigrations'.format(a=a) for a in ma]))
MIGRATION_MODULES = prevent_tests_migrate('default')

# Override settings with local settings.
try:
    from settings_local import *
except ImportError:
    pass
