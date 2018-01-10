import logging

from django.core.management import BaseCommand
from django_geonames.browser.models import City
from importer.importer import CitiesIterator

logger = logging.getLogger('main')


class Command(BaseCommand):
    help = 'Imports cities into database.'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='?', type=str)

    def handle(self, *args, **options):
        with CitiesIterator(options['path']) as cities_iterator:
            for city in cities_iterator:
                logger.info('Saving "{}" city'.format(city.geonameid))
                city_model = City(id=city.geonameid, name=city.name, latitude=city.latitude, longitude=city.longitude,
                                  country_code=city.country_code, county=city.admin2_code)
                city_model.save()
