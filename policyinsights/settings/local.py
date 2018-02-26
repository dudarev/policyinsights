from .base import *


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_ID = 1  # localhost:8000

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'policyinsights',
        'USER': 'policyinsights',
    }
}