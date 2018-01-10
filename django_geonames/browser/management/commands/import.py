from django.core.management import BaseCommand

from importer.importer import CitiesIterator


class Command(BaseCommand):
    help = 'Imports cities into database.'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='?', type=str)

    def handle(self, *args, **options):
        with CitiesIterator(options['path']) as cities_iterator:
            for city in cities_iterator:
                print(city.geonameid)
                print(city.name)
                print(city.latitude)
                print(city.longitude)
                print(city.country_code)
                exit()
