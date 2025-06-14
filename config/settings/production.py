from .base import *

DEBUG = False
SECRET_KEY = env('SECRET_KEY')

DATABASES = {
    'default': env.db(),
}

ALLOWED_HOSTS = ['imageupload-api.fly.dev']

CSRF_TRUSTED_ORIGINS = ['https://imageupload-api.fly.dev/']
