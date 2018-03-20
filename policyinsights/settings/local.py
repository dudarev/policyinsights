from .base import *


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_ID = 1  # localhost:8000

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'policyinsights',
        'USER': 'policyinsights',
        'PASSWORD': 'admin',
    }
}


""" for testing django_db_geventpool
# https://github.com/jneight/django-db-geventpool
# for django 1.6 and newer version, CONN_MAX_AGE must be set to 0, or connections will never go back to the pool
DATABASES['default'].update({
    'ENGINE': 'django_db_geventpool.backends.postgresql_psycopg2',
    'ATOMIC_REQUESTS': False,
    'CONN_MAX_AGE': 0,
    'OPTIONS': {
        'MAX_CONNS': 4,  # 3 workers, 4 connections each, leaving 8 connections out of 20 for one-off tasks
    }})

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware', ] + MIDDLEWARE
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "policyinsights/static/"),
]
"""
