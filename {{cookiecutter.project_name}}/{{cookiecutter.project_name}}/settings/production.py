import os
from .base import *  # NOQA


ALLOWED_HOSTS = [
    "{{cookiecutter.project_name}}.com.ar",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASS"),
        "HOST": os.environ.get("DB_SERVICE"),
        "PORT": os.environ.get("DB_PORT"),
    }
}

