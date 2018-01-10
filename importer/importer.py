import csv
from collections import Iterator


class City:
    # Uses mapping from table defined in http://download.geonames.org/export/dump/readme.txt
    MAP = {
        'geonameid': 0,
        'name': 1,
        'latitude': 4,
        'longitude': 5,
        'country_code': 8,
        'admin2_code': 12
    }

    def __init__(self, row):
        # @TODO Validate if row is correct
        self._data = row

    def __getattr__(self, item):
        # @TODO Check if index exists
        return self._data[self.MAP.get(item)]


class CitiesIterator(Iterator):
    def __init__(self, path):
        self._path = path
        self._fp = None
        self._csv_reader = None

    def __enter__(self):
        self._fp = open(self._path, 'r')
        self._csv_reader = csv.reader(self._fp, delimiter='\t')

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._fp.close()

    def __next__(self):
        return City(next(self._csv_reader))
