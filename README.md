# Django + Django Admin + load data from www.geonames.org

## Installation
Application runs on python `3.6`, tested on MacOS
1. `virtualenv -p /usr/local/bin/python3.6 venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python manage.py migrate`
5. `python manage.py runserver`


## Refactor notes
1. `geonames/importer.py` could be extracted as separated library
