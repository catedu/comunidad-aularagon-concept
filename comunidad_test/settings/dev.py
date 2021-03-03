from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "2kc$a7xhrb##fo=c*o!tef07$6b45uv2j92^ych8zr7=8gtzm#"

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

WAGTAIL_CACHE = False

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "comunida_db",
    }
}

try:
    from .local_settings import *  # noqa
except ImportError:
    pass
