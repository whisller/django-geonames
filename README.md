# Django + Django Admin + load data from www.geonames.org

Simple test app to load data from CSV file to DB and display it inside of Django admin.

## Installation
Application runs on python `3.6`, tested on MacOS
1. `virtualenv -p /usr/local/bin/python3.6 venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python manage.py migrate`
5. `python manage.py createsuperuser`
6. `python manage.py runserver`
7. Visit `http://127.0.0.1:8000/admin/`

## Import of data
1. `python manage.py import ./data/cities15000.txt`

## Check pep8
1. `source venv/bin/activate`
2. `pip install -r requirements_dev.txt`
3. `invoke test`

## Refactor notes
1. `importer` could be extracted as separated library. As it does not belong in here.
