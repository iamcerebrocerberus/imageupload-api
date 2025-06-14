from .base import *

DEBUG = False
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
# Override Cloudinary storage with local file storage
DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
