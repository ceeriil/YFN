#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from decouple import config, UndefinedValueError


PROJECT_NAME = "core"

# For Development use 'settings/development.py'
# For Production use 'settings/production.py'
try:
    DEV = config("DEV", cast=bool)
except UndefinedValueError:
    DEV = True

MODE = "development" if DEV else "production"
SETTINGS_MODULE = f"{PROJECT_NAME}.settings.{MODE}"


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_MODULE)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
