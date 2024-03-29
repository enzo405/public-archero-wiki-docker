from pathlib import Path
from django.utils.translation import gettext_lazy as _
import os

try:
    if os.path.exists('conf/conf_local.py'):
        from conf.conf_local import *
    else:
        from conf.conf import *
except ImportError:
    from conf.conf import *


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = c_SECRET_KEY
DEBUG = c_DEBUG

ALLOWED_HOSTS = c_ALLOWED_HOSTS

INSTALLED_APPS = [
    'calculator.apps.CalculatorConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'calculator.middlewares.wikiMiddleware.CustomHeaderMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

DATABASES = c_DATABASES


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


CSRF_FAILURE_VIEW = c_CSRF_FAILURE_VIEW
CSRF_USE_SESSION = c_CSRF_USE_SESSION
CSRF_COOKIE_SECURE = c_CSRF_COOKIE_SECURE
CSRF_TRUSTED_ORIGINS = c_CSRF_TRUSTED_ORIGINS
CSRF_COOKIE_SAMESITE = c_CSRF_COOKIE_SAMESITE

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "calculator/static/")
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', _('English')),
    ('fr', _('French')),
    ('de', _('German')),
    ('ru', _('Russian')),
    ('br', _('Brazilian')),
)
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)