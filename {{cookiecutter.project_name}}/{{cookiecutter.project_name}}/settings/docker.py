import os
import logging
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

{%- if cookiecutter.huey == "True" %}
HUEY = {
    'name': {{cookiecutter.project_name}},
    'result_store': True,  # Store return values of tasks.
    'events': True,  # Consumer emits events allowing real-time monitoring.
    'store_none': False,  # If a task returns None, do not save to results.
    'always_eager': False, # If DEBUG=True, run synchronously.
    'store_errors': True,  # Store error info if task throws exception.
    'blocking': False,  # Poll the queue rather than do blocking pop.
    'backend_class': 'huey.RedisHuey',  # Use path to redis huey by default,
    'connection': {
        'host': 'redis',
        'port': 6379,
        'db': 0,
        'connection_pool': None,  # Definitely you should use pooling!
        'read_timeout': 1,  # If not polling (blocking pop), use timeout.
        'max_errors': 1000,  # Only store the 1000 most recent errors.
        'url': None,  # Allow Redis config via a DSN.
    },
    'consumer': {
        'workers': 1,
        'worker_type': 'thread',
        'initial_delay': 0.1,  # Smallest polling interval, same as -d.
        'backoff': 5.0,  # Exponential backoff using this rate, -b.
        'max_delay': 10.0,  # Max possible polling interval, -m.
        'utc': True,  # Treat ETAs and schedules as UTC datetimes.
        'scheduler_interval': 10,  # Check schedule every second, -s.
        'periodic': True,  # Enable crontab feature.
        'check_worker_health': True,  # Enable worker health checks.
        'health_check_interval': 5,  # Check worker health every second.
        'loglevel': logging.DEBUG,  # add this.
    },
}

{%- endif %}