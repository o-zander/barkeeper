from .default import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = '*'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database.db',
    }
}