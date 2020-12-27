from django.http import Http404
from django.shortcuts import render
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

from votes.models import Person, Elections, Ingresos, BienMueble, BienInmueble

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def index(request):
    return render(
        request,
        'votes/index.html'
    )

@cache_page(CACHE_TTL)
def ingresos_2021(request):
    election = Elections.objects.get(
        name='Elecciones Generales 2021'
    )
    context = {'election': election}
    persons = []

    for person in Person.objects.filter(elections=election):
        ingresos = Ingresos.objects.filter(
            election=election,
            person=person,
        )
        if ingresos:
            ingreso = ingresos.first()
            person.ingreso = ingreso
            person.ingreso_total = ingreso.decRemuBrutaPublico + \
                ingreso.decRemuBrutaPrivado + \
                ingreso.decRentaIndividualPublico + \
                ingreso.decRentaIndividualPrivado + \
                ingreso.decOtroIngresoPublico + ingreso.decOtroIngresoPrivado
        else:
            person.ingreso_total = 0
        persons.append(person)

    context['candidates'] = sorted(persons, key=lambda x: x.ingreso_total, reverse=True)
    context['ingresos'] = Ingresos.objects.filter(

    )
    return render(
        request,
        'votes/ingresos.html',
        context,
    )


@cache_page(CACHE_TTL)
def bienes_2021(request):
    context, election = make_context()
    persons = []

    for person in Person.objects.filter(elections=election):
        muebles = BienMueble.objects.filter(
            election=election,
            person=person,
        )
        if muebles:
            person.muebles = 0
            for mueble in muebles:
                person.muebles += mueble.decValor
        else:
            person.muebles = 0

        inmuebles = BienInmueble.objects.filter(
            election=election,
            person=person,
        )
        if inmuebles:
            person.inmuebles = 0
            for inmueble in inmuebles:
                person.inmuebles += inmueble.decAutovaluo
        else:
            person.inmuebles = 0

        person.total_muebles_inmuebles = person.inmuebles + person.muebles
        persons.append(person)

    context['candidates'] = sorted(persons, key=lambda x: x.total_muebles_inmuebles, reverse=True)
    context['ingresos'] = Ingresos.objects.filter(

    )
    return render(
        request,
        'votes/bienes.html',
        context,
    )


def make_context():
    election = Elections.objects.get(
        name='Elecciones Generales 2021'
    )
    context = {'election': election}
    return context, election


def candidato_2021(request, dni):
    context, election = make_context()
    person = Person.objects.filter(
        dni_number=dni,
        elections=election,
    )
    if not person:
        raise Http404(f'no tenemos candidato con ese dni {dni}')

    person = person.first()
    context['candidate'] = person
    context['muebles'] = BienMueble.objects.filter(
        person=person,
        election=election,
    )
    context['inmuebles'] = BienInmueble.objects.filter(
        person=person,
        election=election,
    )
    context['ingresos'] = Ingresos.objects.filter(
        person=person,
        election=election,
    ).first()
    if context['ingresos']:
        context['ingresos_total'] = context['ingresos'].decRemuBrutaPublico + \
                                    context['ingresos'].decRemuBrutaPrivado + \
                                    context['ingresos'].decRentaIndividualPublico + \
                                    context['ingresos'].decRentaIndividualPrivado
    return render(
        request,
        'votes/candidate.html',
        context,
    )
