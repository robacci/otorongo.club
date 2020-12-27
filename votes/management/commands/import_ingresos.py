import json
import csv

from django.core.management import BaseCommand

from votes.models import Elections, HojaVida, BienInmueble, Person, BienMueble, Ingresos


class Command(BaseCommand):
    help = "Import ingresos 2021 from CSV file"

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
    ingreso, created = Ingresos.objects.get_or_create(
        idHVIngresos=item['idHVIngresos']
    )
    if created:
        print(f'created {ingreso}')

    ingreso.idHojaVida = hoja_vida
    ingreso.election = election
    ingreso.person = person

    ingreso.idEstado = item['idEstado']
    ingreso.decRemuBrutaPublico = item['decRemuBrutaPublico']
    ingreso.decRemuBrutaPrivado = item['decRemuBrutaPrivado']
    ingreso.decRentaIndividualPublico = item['decRentaIndividualPublico']
    ingreso.decRentaIndividualPrivado = item['decRentaIndividualPrivado']
    ingreso.decOtroIngresoPublico = item['decOtroIngresoPublico']
    ingreso.decOtroIngresoPrivado = item['decOtroIngresoPrivado']
    ingreso.strUsuario = item['strUsuario']
    ingreso.strTengoIngresos = item['strTengoIngresos']
    ingreso.strAnioIngresos = item['strAnioIngresos']
    ingreso.save()
