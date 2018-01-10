from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Imports cities into database.'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, *args, **options):
        pass
