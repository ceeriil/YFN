# flake8: noqa

from core.settings.base import *
import dj_database_url
from decouple import config


# Include your hosts here
ALLOWED_HOSTS = ["*"]

# Redirect non-ssl requests to ssl version.
SECURE_SSL_REDIRECT = True

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': ''
#     }
# }

# create db dictionary with dj_database_url from DATABASE_URL
postgres_db = dj_database_url.parse(config("DATABASE_URL"), conn_max_age=600)
# DATABASES = {} is declared in the base.py
DATABASES["default"] = postgres_db

# STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY')
# STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY')
