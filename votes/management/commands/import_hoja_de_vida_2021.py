import json
from time import sleep
import requests

from django.core.management import BaseCommand
from parsel import Selector

from votes.models import Person, Elections, HojaVida


class Command(BaseCommand):
    help = "Import hojas de vida 2021"

    def add_arguments(self, parser):
        parser.add_argument('-i', '--input', action='store')

    def handle(self, *args, **options):
        input_file = options['input']
        import_data(input_file)


def import_data(input_file):
    print(f"processing {input_file}")
    election = Elections.objects.get(name='Elecciones Generales 2021')

    with open(input_file) as handle:
        content = handle.read()
        items = json.loads(content)

        for item in items:
            process_item(item, election)


def process_item(item, election):
    fields = item['fields']
    hoja_de_vida_id = fields["idHojaVida"]
    hoja, created = HojaVida.objects.get_or_create(idHojaVida=hoja_de_vida_id)

    if created:
        print(f'Created {hoja}')

    hoja.election = election
    hoja.save()
