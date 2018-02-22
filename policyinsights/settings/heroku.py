# https://devcenter.heroku.com/articles/django-app-configuration
import dj_database_url

from .base import *

SITE_ID = 2  # Heroku staging

# Change 'default' database configuration with $DATABASE_URL.
DATABASES['default'].update(dj_database_url.config(conn_max_age=500))

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