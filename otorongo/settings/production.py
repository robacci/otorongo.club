import os

from .base import *


DATABASES["default"]["USER"] = "postgres"
DATABASES["default"]["HOST"] = "db"


ALLOWED_HOSTS = [
    '.otorongo.club',  # Allow domain and subdomains
    '.otorongo.club.',  # Also allow FQDN and subdomains
]

MEDIA_ROOT = "/data/media/"
STATIC_ROOT = "/data/static/"

DEBUG = False
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
