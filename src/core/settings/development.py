# flake8: noqa

from core.settings.base import *
from decouple import config, UndefinedValueError

# SECURITY WARNING: don't run with debug turned on in production!
# If the DEBUG is not set in development, it will be True.
try:
    DEBUG = config("DEBUG", cast=bool)
except UndefinedValueError:
    DEBUG = True

# Including '127.0.0.1' for debug_toolbar
ALLOWED_HOSTS = ["127.0.0.1", "djb1.herokuapp.com"]

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE += [
    # For debug_toolbar
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# DEBUG TOOLBAR SETTINGS

DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
]


# Show or hide debug_toolbar
def show_toolbar(request):
    return DEBUG


DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}

# DATABASES = {} is declared in the base.py
DATABASES["default"] = {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": BASE_DIR / "db.sqlite3",
}

# STRIPE_PUBLIC_KEY = config('STRIPE_TEST_PUBLIC_KEY')
# STRIPE_SECRET_KEY = config('STRIPE_TEST_SECRET_KEY')
