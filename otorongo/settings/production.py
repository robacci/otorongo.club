from .base import *


DATABASES["default"]["USER"] = "postgres"
DATABASES["default"]["HOST"] = "db"

ALLOWED_HOSTS = ['localhost', 'otorongo.club']
