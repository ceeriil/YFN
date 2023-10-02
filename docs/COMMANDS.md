```bash
conda remove --name env_dj --all
conda create --name env_dj python=3.7
conda activate env_dj
pip install -r requirements.txt
pip freeze > requirements.txt

pip install django
pip install django-debug-toolbar
pip install python-decouple

django-admin startproject core
python manage.py startapp app
```
