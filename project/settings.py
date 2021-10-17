import os

from environs import Env
import dj_database_url

env = Env()
env.read_env()

debug = env.bool('DEBUG')
db_url = env.str('DB_URL')
secret_key = env.str('SECRET_KEY')
allowed_hosts = env.list('ALLOWED_HOSTS')

DATABASES = {
    'default': dj_database_url.parse(db_url)
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = secret_key

DEBUG = debug

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = allowed_hosts

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
