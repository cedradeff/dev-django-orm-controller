from dotenv import load_dotenv
import dj_database_url
import os

load_dotenv()

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get("DB_URL")
    )
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = 'REPLACE_ME'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
