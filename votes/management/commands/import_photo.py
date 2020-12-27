import base64
import requests

from django.core.management import BaseCommand

from votes.models import Elections, HojaVida, BienInmueble, Person, Image


class Command(BaseCommand):
    help = "Import photo 2021 from CSV file"

    def handle(self, *args, **options):
        import_data()


def import_data():
    print("processing")
    election = Elections.objects.get(name='Elecciones Generales 2021')
    persons = Person.objects.filter(elections=election)

    base_url = 'https://declara.jne.gob.pe'

    for person in persons:
        url = f'{base_url}{person.strRutaArchivo}'
        print(person, url)
        response = requests.get(url)
        encoded = base64.b64encode(response.content).decode("utf-8")
        image = Image.objects.create(
            image=encoded
        )
        person.photo = image
        person.save()
