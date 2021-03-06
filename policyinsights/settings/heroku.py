# https://devcenter.heroku.com/articles/django-app-configuration
import dj_database_url

from .base import *

SITE_ID = 2  # Heroku staging

# Change 'default' database configuration with $DATABASE_URL.
DATABASES['default'].update(dj_database_url.config())

# https://github.com/jneight/django-db-geventpool
# for django 1.6 and newer version, CONN_MAX_AGE must be set to 0, or connections will never go back to the pool
DATABASES['default'].update({
        'ENGINE': 'django_db_geventpool.backends.postgresql_psycopg2',
        'ATOMIC_REQUESTS': False,
        'CONN_MAX_AGE': 0,
        'OPTIONS': {
            'MAX_CONNS': 3,  # 3 workers, 3 connections each, leaving 11 connections out of 20 for one-off tasks
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

# https://sendgrid.com/docs/Integrate/Frameworks/django.html
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME', '')
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD', '')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'admin@policyinsights.us'