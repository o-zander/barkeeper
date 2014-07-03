import os
from django.conf import global_settings as DEFAULT_SETTINGS

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = 'w0jum9+6)jrw=sd1+tk%pz#mm45c*e)ve6@9=awor)5u#$9wqc'

ROOT_URLCONF = 'barkeeper.urls'

WSGI_APPLICATION = 'barkeeper.wsgi.application'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

LANGUAGE_CODE = 'de-DE'
TIME_ZONE = 'Europe/Berlin'

USE_I18N = True
USE_L10N = True
USE_TZ = True

DECIMAL_SEPARATOR = ','
THOUSAND_SEPARATOR = '.'

LOCALE_PATHS = (os.path.join(ROOT_DIR, 'conf', 'locale'),)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ROOT_DIR, 'media')

TEMPLATE_LOADERS = ('django.template.loaders.app_directories.Loader',)

STATICFILES_FINDERS = ('django.contrib.staticfiles.finders.AppDirectoriesFinder',)
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

INSTALLED_APPS = (
    # Main
    'barkeeper',

    # Contrib
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Tools
    'pipeline',
)

PIPELINE_CSS = {
    'base': {
        'source_filenames': ('less/custom-style.less',),
        'output_filename': 'css/custom-style.css',
        'extra_context': {'media': 'all'},
    },
}

PIPELINE_COMPILERS = ('pipeline.compilers.less.LessCompiler',)