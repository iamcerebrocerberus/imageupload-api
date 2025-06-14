from .base import *


DATABASES = {
    'default': env.db(),
}
DEBUG = env.bool("DEBUG", default=True)
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

STATIC_ROOT = BASE_DIR / "staticfiles"
INSTALLED_APPS += ["whitenoise.runserver_nostatic", "debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
INTERNAL_IPS = [
    "127.0.0.1",
]

# DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': env('CLOUDINARY_API_KEY'),
    'API_SECRET': env('CLOUDINARY_API_SECRET'),
}
