from django.core.management import BaseCommand

from votes.models import Elections, Person, Ingresos, CompiledPerson


class Command(BaseCommand):
    help = "Compile data for candidates. Computing all data in the fly is too costly"

    def handle(self, *args, **options):
        process()


def process():
    print("processing")

    election = Elections.objects.get(
        name='Elecciones Generales 2021'
    )
    for person in Person.objects.filter(elections=election):
        compiled_person, created = CompiledPerson.objects.get_or_create(
            person=person
        )
        if created:
            print(f'created {compiled_person}')
        ingresos = Ingresos.objects.filter(
            election=election,
            person=person,
        )
        if ingresos:
            ingreso = ingresos.first()
            compiled_person.ingreso = ingreso
            compiled_person.ingreso_total = \
                ingreso.decRemuBrutaPublico + \
                ingreso.decRemuBrutaPrivado + \
                ingreso.decRentaIndividualPublico + \
                ingreso.decRentaIndividualPrivado + \
                ingreso.decOtroIngresoPublico + \
                ingreso.decOtroIngresoPrivado
        else:
            compiled_person.ingreso_total = 0

        compiled_person.save()
