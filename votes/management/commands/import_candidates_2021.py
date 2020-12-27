import json
from time import sleep
import requests

from django.core.management import BaseCommand
from parsel import Selector

from votes.models import Person, Elections


class Command(BaseCommand):
    help = "Import candidates 2021"

    def add_arguments(self, parser):
        parser.add_argument('-i', '--input', action='store')

    def handle(self, *args, **options):
        input_file = options['input']
        import_candidates(input_file)


def import_candidates(input_file):
    print(f"processing {input_file}")
    election = Elections.objects.get(name='Elecciones Generales 2021')

    with open(input_file) as handle:
        content = handle.read()
        items = json.loads(content)

        for item in items:
            process_item(item, election)


def process_item(item, election):
    fields = item['fields']
    dni_number = fields['strDocumentoIdentidad']
    first_names = fields['strNombres']
    last_names = f"{fields['strApellidoPaterno']} {fields['strApellidoMaterno']}"

    person, created = Person.objects.get_or_create(dni_number=dni_number)
    if created:
        print(f'Created {person}')
    person.elections.add(election)
    person.first_names = first_names
    person.last_names = last_names
    person.save()

    Person.objects.filter(id=person.id).update(**fields)
    person.refresh_from_db()
    print(person.strDocumentoIdentidad)

