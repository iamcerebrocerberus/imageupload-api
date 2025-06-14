from .base import *

DEBUG = False
SECRET_KEY = env('SECRET_KEY')

DATABASES = {
    'default': env.db(),
}

ALLOWED_HOSTS = ['imageupload-api.fly.dev']

CSRF_TRUSTED_ORIGINS = ['https://imageupload-api.fly.dev/']

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': env('CLOUDINARY_API_KEY'),
    'API_SECRET': env('CLOUDINARY_API_SECRET'),
}
