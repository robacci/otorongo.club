import json
import csv

from django.core.management import BaseCommand

from votes.models import Elections, HojaVida, BienInmueble, Person, BienMueble


class Command(BaseCommand):
    help = "Import muebles 2021 from CSV file"

    def add_arguments(self, parser):
        parser.add_argument('-i', '--input', action='store')

    def handle(self, *args, **options):
        input_file = options['input']
        import_data(input_file)


def import_data(input_file):
    print(f"processing {input_file}")
    election = Elections.objects.get(name='Elecciones Generales 2021')

    with open(input_file) as csvfile:
        reader = csv.DictReader(csvfile)
        for item in reader:
            process_item(item, election)


def process_item(item, election):
    hoja_de_vida_id = item["idHojaVida_idHojaVida"]
    hoja_vida = HojaVida.objects.get(idHojaVida=hoja_de_vida_id)
    person = Person.objects.get(idHojaVida=hoja_vida)

    print('**', hoja_vida)
    del item['idHojaVida_idHojaVida']
    del item['idHojaVida_id']
    mueble, created = BienMueble.objects.get_or_create(
        idHVBienMueble=item['idHVBienMueble']
    )
    if created:
        print(f'created {mueble}')

    mueble.idHojaVida = hoja_vida
    mueble.election = election
    mueble.person = person

    mueble.intItemMueble = item['intItemMueble']
    mueble.idEstado = item['idEstado']
    mueble.decValor = item['decValor']
    mueble.strTengoBienMueble = item['strTengoBienMueble']
    mueble.strVehiculo = item['strVehiculo']
    mueble.strMarca = item['strMarca']
    mueble.strPlaca = item['strPlaca']
    mueble.strUsuario = item['strUsuario']
    mueble.strModelo = item['strModelo']
    mueble.strAnio = item['strAnio']
    mueble.strCaracteristica = item['strCaracteristica']
    mueble.strOrder = item['strOrder']
    mueble.strComentario = item['strComentario']
    mueble.save()
