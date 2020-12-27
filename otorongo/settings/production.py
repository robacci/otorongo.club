from .base import *


DATABASES["default"]["USER"] = "postgres"
DATABASES["default"]["HOST"] = "db"

ALLOWED_HOSTS = ['localhost', 'otorongo.club']

MEDIA_ROOT = "/data/media/"
STATIC_ROOT = "/data/static/"

DEBUG = False
