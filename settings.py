import os

import dj_database_url
from dotenv import load_dotenv
load_dotenv()

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INSTALLED_APPS = (
    'data',
)
# settings for postgres database
DATABASES = {}
DATABASES['default'] = dj_database_url.config(
    default="postgres://{user}:{password}@{host}:{port}/{name}".format(
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD"),
        host=os.getenv("DATABASE_HOST"),
        port=os.getenv("DATABASE_PORT"),
        name=os.getenv("DATABASE_NAME")
    ), 
    conn_max_age=600
)
if os.getenv("DATABASE_SCHEMA") is not None:
    options = {}
    options["options"] = "-c search_path={schema}".format(
        schema=os.getenv("DATABASE_SCHEMA")
    )
    DATABASES["default"]["OPTIONS"] = options

SECRET_KEY = 'REPLACE_ME'
