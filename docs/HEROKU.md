# Heroku

## heroku CLI

## Commands

```sh

# logs
heroku logs --app djb1 --tail

# run
heroku run -a djb1 "python src/manage.py migrate"
heroku run -a djb1 "gunicorn --pythonpath src djpro.wsgi --log-file -"
```

## Configure Project for Heroku

- Create the following files in the root directory.
  - requirements.txt
  - Procfile
  - runtime.txt

- Procfile
  - Here project name is core. And core is situated inside src directory.
  - Reference: https://devcenter.heroku.com/articles/release-phase

  ```sh
  release: python src/manage.py migrate
  web: gunicorn --pythonpath src core.wsgi --log-file -
  ```

## Whitenoise Configuration

Reference: https://devcenter.heroku.com/articles/django-assets

### Installation

```sh
pip install whitenoise
```

### settings.py

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

MIDDLEWARE = [
    # Part of base
    'django.middleware.security.SecurityMiddleware',

    # From WhiteNoise to serve static files in Heroku from Django
    # Remove this if you are using S3
    'whitenoise.middleware.WhiteNoiseMiddleware',

    # Part of base
    'django.contrib.sessions.middleware.SessionMiddleware',
    '...',
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'

# Keep your static files here.
# collectstatic will use this directory to generate static files in STATIC_ROOT.
STATICFILES_DIRS = [BASE_DIR / 'static']
```

> Django won’t automatically create the target directory (STATIC_ROOT) that `collectstatic` uses, if it isn’t available.
You may need to create this directory in your codebase, so it will be available when `collectstatic` is run.
Git does not support empty file directories, so you will have to create a file inside that directory as well.

## Allowed Hosts

```python
ALLOWED_HOSTS = ["*"]
```

## Environmental Variables

### Production

- `DEV = False`
- SECRET_KEY = YOUR_DJANGO_SECRET_KEY
- DATABASE_URL = YOUR_DATABASE_URL
> `DEV = True` can be used to run production in debug mode.

### Development

- Configuration not required.
- By default, `DEV = True, DEBUG = True`.
> `DEBUG = False` can be used to hide Debug Toolbar.

## Deploying in Heroku

- Run `python src/manage.py makemigrations` before pushing the repository to git.
- Create an app in Heroku and attach the git repository with it.
- Set environment variable `DEV = False`
- In the heroku console, run the following commands.

```shell
python ./src/manage.py migrate  # Already executed with Profile.
python ./src/manage.py createsuperuser
```

## Connect the Heroku PostgresSQL DB to local pgAdmin

- Get the DATABASE_URL from Heroku
- DATABASE_URL = postgres://username:password@host:port/db_name
- In the pgAdmin, connect ot the PostgreSQL server using the credentials.
