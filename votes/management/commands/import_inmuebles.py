import json
import csv

from django.core.management import BaseCommand

from votes.models import Elections, HojaVida, BienInmueble, Person


class Command(BaseCommand):
    help = "Import inmuebles 2021 from CSV file"

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
    inmueble, created = BienInmueble.objects.get_or_create(
        idHVBienInmueble=item['idHVBienInmueble']
    )
    if created:
        print(f'created {inmueble}')

    inmueble.idHojaVida = hoja_vida
    inmueble.election = election
    inmueble.person = person

    inmueble.intItemInmueble = item['intItemInmueble']
    inmueble.decAutovaluo = item['decAutovaluo']
    inmueble.idEstado = item['idEstado']
    inmueble.decUIT = item['decUIT']
    inmueble.strTengoInmueble = item['strTengoInmueble']
    inmueble.strTipoBienInmueble = item['strTipoBienInmueble']
    inmueble.strUbigeoInmueble = item['strUbigeoInmueble']
    inmueble.strInmuebleUbiDepartamento = item['strInmuebleUbiDepartamento']
    inmueble.strInmuebleUbiProvincia = item['strInmuebleUbiProvincia']
    inmueble.strInmuebleUbiDistrito = item['strInmuebleUbiDistrito']
    inmueble.strInmueblePais = item['strInmueblePais']
    inmueble.strInmuebleDepartamento = item['strInmuebleDepartamento']
    inmueble.strInmuebleProvincia = item['strInmuebleProvincia']
    inmueble.strInmuebleDistrito = item['strInmuebleDistrito']
    inmueble.strInmuebleDireccion = item['strInmuebleDireccion']
    inmueble.strInmuebleSunarp = item['strInmuebleSunarp']
    inmueble.strPartidaSunarp = item['strPartidaSunarp']
    inmueble.strFichaTomoSunarp = item['strFichaTomoSunarp']
    inmueble.strUsuario = item['strUsuario']
    inmueble.strOrder = item['strOrder']
    inmueble.strComentario = item['strComentario']
    inmueble.save()
