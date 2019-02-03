import os

from .base import *  # NOQA

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', "postgres"),
        'USER': os.environ.get('DB_USER', "postgres"),
        'PASSWORD': os.environ.get('DB_PASS', "secret"),
        'HOST': os.environ.get('DB_SERVICE', "postgres"),
        'PORT': os.environ.get('DB_PORT', 5432),
    }
}
