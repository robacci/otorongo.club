from django.contrib.postgres.search import SearchQuery
from django.core.paginator import InvalidPage
from django.http import Http404
from django.shortcuts import render
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

from votes.models import Person, Elections, Ingresos, BienMueble, BienInmueble, CompiledPerson
from votes.utils import Paginator

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def index(request):
    return render(
        request,
        'votes/index.html'
    )


@csrf_exempt
def search(request):
    context, election = make_context()
    query = request.GET.get('q') or ''
    query = query.strip()

    all_items = Person.objects.filter(
        full_search=SearchQuery(query),
        elections=election,
    )
    print(all_items)
    context['all_items'] = all_items
    context['all_items_count'] = all_items.count()
    context['query'] = query

    return render(
        request,
        'votes/search.html',
        context,
    )


def ingresos_2021(request):
    election = Elections.objects.get(
        name='Elecciones Generales 2021'
    )
    context = {'election': election}

    persons = CompiledPerson.objects.filter(
        person__elections=election,
    ).order_by('-ingreso_total')

    paginator, page = do_pagination(request, persons)
    context['candidates'] = paginator
    context['page'] = page

    return render(
        request,
        'votes/ingresos.html',
        context,
    )


def sentencias_2021(request):
    context, election = make_context()
    persons = CompiledPerson.objects.filter(
        person__elections=election,
    ).order_by('-sentencias_total')

    paginator, page = do_pagination(request, persons)
    context['candidates'] = paginator
    context['page'] = page

    return render(
        request,
        'votes/sentencias.html',
        context,
    )


def bienes_2021(request):
    context, election = make_context()

    persons = CompiledPerson.objects.filter(
        person__elections=election
    ).order_by('-total_muebles_inmuebles')

    paginator, page = do_pagination(request, persons)
    context['candidates'] = paginator
    context['page'] = page

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
                                    context['ingresos'].decRentaIndividualPrivado + \
                                    context['ingresos'].decOtroIngresoPublico + \
                                    context['ingresos'].decOtroIngresoPrivado
    context['sentencias_penal'] = person.sentenciapenal_set.all()
    context['sentencias_obliga'] = person.sentenciaobliga_set.all()
    return render(
        request,
        'votes/candidate.html',
        context,
    )


def do_pagination(request, all_items):
    """
    :param request: contains the current page requested by user
    :param all_items:
    :return: dict containing paginated items and pagination bar
    """
    results_per_page = 50
    results = all_items

    try:
        page_no = int(request.GET.get('page', 1))
    except (TypeError, ValueError):
        raise Http404("Not a valid number for page.")

    if page_no < 1:
        raise Http404("Pages should be 1 or greater.")

    paginator = Paginator(results, results_per_page)

    try:
        page = paginator.page(page_no)
    except InvalidPage:
        raise Http404("No such page!")

    return paginator, page
