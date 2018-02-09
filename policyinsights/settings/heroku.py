# https://devcenter.heroku.com/articles/django-app-configuration
import dj_database_url

from .base import *


# Change 'default' database configuration with $DATABASE_URL.
DATABASES['default'].update(dj_database_url.config(conn_max_age=500))

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware', ] + MIDDLEWARE
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
