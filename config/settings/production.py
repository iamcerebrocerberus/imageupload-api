from .base import *

DEBUG = False
SECRET_KEY = env('SECRET_KEY')

DATABASES = {
    'default': env.db(),
}

ALLOWED_HOSTS = ['imageupload-api.fly.dev']

CSRF_TRUSTED_ORIGINS = ['https://imageupload-api.fly.dev/']

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
