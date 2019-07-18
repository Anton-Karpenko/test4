from django.core.management import BaseCommand

from apps.apartment_advt.parsers import DomRiaParser


class Command(BaseCommand):

    def handle(self, *args, **options):
        DomRiaParser().parse()
