import os
import dj-database-url

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INSTALLED_APPS = (
    'data',
)
# settings for postgres database
DATABASES = {}
DATABASES['default'] = dj_database_url.config(
    default="postgres://user:password@host:port/name", 
    conn_max_age=600
)

SECRET_KEY = 'REPLACE_ME'
