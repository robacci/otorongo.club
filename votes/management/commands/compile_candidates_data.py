from django.core.management import BaseCommand

from votes.models import Elections, Person, Ingresos, CompiledPerson, BienMueble, BienInmueble


class Command(BaseCommand):
    help = "Compile data for candidates. Computing all data in the fly is too costly"

    def handle(self, *args, **options):
        process()


def process():
    print("processing")
    process_ingresos()
    process_bienes()


def process_bienes():
    election = Elections.objects.get(
        name='Elecciones Generales 2021'
    )
    for person in Person.objects.filter(elections=election):
        compiled_person, created = CompiledPerson.objects.get_or_create(
            person=person
        )
        if created:
            print(f'created {compiled_person}')
        muebles = BienMueble.objects.filter(
            election=election,
            person=person,
        )
        if muebles:
            compiled_person.muebles = 0
            for mueble in muebles:
                compiled_person.muebles += mueble.decValor
        else:
            compiled_person.muebles = 0

        inmuebles = BienInmueble.objects.filter(
            election=election,
            person=person,
        )
        if inmuebles:
            compiled_person.inmuebles = 0
            for inmueble in inmuebles:
                compiled_person.inmuebles += inmueble.decAutovaluo
        else:
            compiled_person.inmuebles = 0

        compiled_person.total_muebles_inmuebles = compiled_person.inmuebles + compiled_person.muebles
        compiled_person.save()


def process_ingresos():
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
