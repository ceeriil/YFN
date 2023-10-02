# Note on Django Boilerplate Project

## Lesson 1 - Setting up the Debug Toolbar

### Section 1.1 - Project Initialization

- Install miniconda from [here](https://docs.conda.io/en/latest/miniconda.html)
- Create and activate a virtual environment.

```bash
prompt $g
conda remove --name env_dj --all
conda create --name env_dj python=3.7
conda activate env_dj
pip install -r requirements.txt
pip freeze > requirements.txt
```

- Install Django. `pip install django`
- Start a project named 'basepro'. `django-admin startproject basepro`
- It will create a directory 'basepro' having all the related files.
- Rename this 'basepro' to 'src'.

### Section 1.2 - Installing Django Debug Toolbar

Django Debug Toolbar is used to have a look at the underlying information.
[Installation](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)

- Install DDT. `pip install django-debug-toolbar`
- Include 'debug_toolbar' in the INSTALLED_APPS of src/basepro/settings.py
- Include the following lines in the settings.py.

```bash
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_files')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Media files (Uploaded by the users)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

- Create directory 'src/static_files'
- Add this on the bottom of basepro/urls.py

```python
from django.conf import settings
from django.urls import include, path


if settings.DEBUG:
    import debug_toolbar

    # For Django Debug Toolbar in debug mode.
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

    # To serve static files in debug mode
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

    # To serve media files in debug mode
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
```

- Add DDT MIDDLEWARE in settings.py.
- For development edit ALLOWED_HOSTS in settings.py. This is needed to run the DDT in debug mode.

```python
ALLOWED_HOSTS = ['127.0.0.1',]
```

- Add DEBUG_TOOLBAR_PANELS to settings.py from [here](https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html)
- Add DEBUG_TOOLBAR_CONFIG in settings.py
- [Optional] You can run collectstatic command to fetch all the django backend static files. In will create src/static_root directory with other directories like admin, debug_toolbar, etc.
[More Info](https://docs.djangoproject.com/en/3.1/ref/contrib/staticfiles/).
`python manage.py collectstatic`

### Section 1.3 - Configure templates

- On the top of settings.py under BASE_DIR, add TEMPLATE_DIR.
```python
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
```

- Edit DIRS of TEMPLATES in settings.py
```python
TEMPLATES = [
    {
        # ...
        'DIRS': [TEMPLATE_DIR],
        # ...
    },
]
```

- Create directory 'src/templates'
- Create 'src/templates/core/base.html' and 'src/templates/core/home.html'. We are keeping these html files inside core to keep all templates according to the apps.
- Create directory 'src/media'

## Lesson 2 - Setting up Multiple Settings Modules

We want to keep the settings.py as much as readable. Writing development settings and production settings in the same file makes it very large. Thus, with this technique we are going to decouple everthing and structure the settings in a better way.

- Create directory 'basepro/settings'
- Create 'basepro/settings/__init__.py' to enable file referencing in this directory.
- Create 'basepro/settings/base.py' where the default django settings and important settings will be stored. This is the common settings for development and production. Copy everthing from settings.py to base.py and delete the settings.py.
- Create 'basepro/settings/development.py' and 'basepro/settings/production.py' for development and production respectively.
- In base.py update the BASE_DIR as we have moved our settings file one directory down.

```python
# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Customized the BASE_DIR as changed settings.py to settings directory.
# By this we are selecting src as BASE_DIR.
# Present file name is base.py. Parent of base.py is settings.
# settings -> parent -> <directory> -> parent -> src.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
```

- Extend development.py and production.py from base.py by including this in both the files. This way, development.py and production.py will keep all the settings of base.py and add few more settings to the existing settings.

```python
from .base import *
```

- Move DEBUG and ALLOWED_HOSTS variables in development.py and production.py. These variables will will defer from each other based development or production.
- We need debug_toolbar and the following middleware only on development mode. Thus, move these from base.py to development.py. Also add the DEBUG TOOLBAR SETTINGS here.

```python
INSTALLED_APPS += [
    'debug_toolbar'
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

# DEBUG TOOLBAR SETTINGS
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar
}
```

- Configure development.py and production.py based on the needs.
- We'll use sqlite for development and postgres for production.
- Important for production. DEBUG=False and change ALLOWED_HOSTS doesn't contain the 127.0.0.1 or localhost.

## Lesson 3 - How to Use Python Decouple
We don't want to hard code our confidentials information.
Python Decouple is used to safely fetch the confidentials keys from .env or OS. [More Info](https://pypi.org/project/python-decouple/)

- Install Python Decouple

```bash
pip install python-decouple
```

- For development create 'src/.env'. Python Decouple will fetch the keys from here if exists.
- Order of search by Decouple: 1. Environment variables, 2. Repository: ini or .env file, 3. Default argument passed to config.
- Add '.env' to the .gitignore so that this file is not saved in the git repository. When you initiate Python .gitignore in GitHub, this is automatically added. But check it once.
- In development Decouple will fetch the env variables from .env file.
- In Heroku, you can add the env variables manually. That time Decouple will fetch the keys from the OS.
- Edit src/manage.py to select the correct settings based on development or production.

```python
import os
from decouple import config


# For Development use 'basepro/settings/development.py'
# For Production use 'basepro/settings/production.py'
PROJECT_NAME = 'basepro'

# For Development use 'settings/development.py'
# For Production use 'settings/production.py'
DEBUG = config('DEBUG', cast=bool)

if DEBUG:
    SETTINGS_MODULE = f'{PROJECT_NAME}.settings.development'
else:
    SETTINGS_MODULE = f'{PROJECT_NAME}.settings.production'


def main():
    # ...
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', SETTINGS_MODULE)
    # ...
```

## Lesson 4 - How to Create Custom Django Commands
We use `python manage.py command` to execute a command. We can add our custom commands this way.
To create custom command(s), we must create an app. We can name our main app as 'core' or 'main'.

- Create an app 'core'

```bash
python manage.py startapp core
# or
django-admin startapp core
```

- Create 'core/management/commands/rename.py'. Here 'rename' is our command, thus we create this py file here.
- The management directory can't be in basepro which is our project directory. It has to be inside an app.
- Create Command class in this file to make the command.
- If you type this command, you can get information regarding all the commands. You can also notice rename command listed under core.

```bash
python manage.py help
```

- In the add_arguments() method of Command class, if you name an argument with dash('-') at the beginning, then it will be an optional commands.

```python
parser.add_argument('-p', '--prefix', type=str, help='Info to help.')
```

- Write the logic and finish writing the code for rename command.

## Extra

### Section X.1 - Configure basepro/urls.py

- Edit basepro/urls.py

```python
urlpatterns = [
    ...
    path('', include('core.urls', namespace='core'))
    ...
]
```

- Edit core/urls.py

```python
from django.urls import path
from .views import HomeView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
```

- Edit core/views.py

```python
from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "core/home.html"
```

### Section X.2 - Refactor asgi.py and wsgi.py in the Project Directory

In production, this is wsgi.py is used to run the app.
We import the SETTINGS_MODULE that is defined in the manage.py.

```python
from manage import SETTINGS_MODULE

os.environ.setdefault('DJANGO_SETTINGS_MODULE', SETTINGS_MODULE)
```

### Section X.3 - Refactor settings/base.py in the Project Directory

Import PROJECT_NAME from manage.py and replace the project name string with this.
```python
from manage import PROJECT_NAME
```

## Important
- For testing purpose '.env' is commented inside .gitignore. Uncomment that just after cloning this repository.
- During production, set environment variable DEBUG=True as this will select the productions settings.
