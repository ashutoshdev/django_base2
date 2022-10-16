from config.settings.base import *
from config.settings.base import env


SECRET_KEY = env('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = ['*']
DOMAINS_WHITELIST = ['*']

DATABASES = {"default": env.db("DATABASE_URL")}

DATABASES["default"]["ATOMIC_REQUESTS"] = True

STATIC_ROOT = str(ROOT_DIR / "staticfiles")

STATIC_URL = "/static/"

STATICFILES_DIRS = [str(APPS_DIR / "static")]

MEDIA_ROOT = str(APPS_DIR / "media")

MEDIA_URL = "/media/"
