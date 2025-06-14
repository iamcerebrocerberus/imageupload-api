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
