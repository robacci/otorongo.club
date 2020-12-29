from time import sleep

from django.core.management.base import BaseCommand
import requests

from votes.models import Person, Elections, SentenciaPenal, SentenciaObliga, Department, Expediente, \
    HojaVida


class Command(BaseCommand):
    help = "Crawl candidates from JNE page."

    def add_arguments(self, parser):
        parser.add_argument('-cl', '--crawl_lists_candidates', action='store_true',
                            help='crawl lists candidates')
        parser.add_argument('-ucl', '--update_candidates_in_lists', action='store_true',
                            help='update candidates in lists')
        parser.add_argument('-ccl', '--crawl_candidates_in_lists', action='store_true',
                            help='crawl candidates in lists')
        parser.add_argument('-csp', '--crawl_sentencia_penal', action='store_true',
                            help='crawl sentencia penal')
        parser.add_argument('-cso', '--crawl_sentencia_obliga', action='store_true',
                            help='crawl sentencia obliga')

    def handle(self, *args, **options):
        if options.get("crawl_lists_candidates"):
            crawl_lists_candidates()
        elif options.get('update_candidates_in_lists'):
            update_candidates_in_lists()
        elif options.get("crawl_candidates_in_lists"):
            crawl_candidates_in_lists()
        elif options.get("crawl_sentencia_penal"):
            crawl_sentencia_penal()
        elif options.get("crawl_sentencia_obliga"):
            crawl_sentencia_obliga()


def crawl_lists_candidates():
    print("Crawl lists of candidates")

    # get lista de expedientes
    url = ("https://plataformaelectoral.jne.gob.pe/Expediente/"
           "BusquedaReporteAvanzadoExpediente")
    payload = {'idJuradoElectoral': 0,
               'idOrganizacionPolitica': 0,
               'idProcesoElectoral': 110,
               'idTipoExpediente': 13,
               'strUbigeo': '000000'}
    res = requests.post(url, data=payload)
    data = res.json()
    unique_ids = set()

    for i in data.get("data"):
        unique_ids.add(i['idExpediente'])

    print(f'got {len(data["data"])} expedientes')
    print(f'got unique {len(unique_ids)} expedientes')

    for item in data.get("data"):
        department, _ = Department.objects.get_or_create(name=item["strDepartamento"])

        defaults = {
            "str_cod_expediente_ext": item["strCodExpedienteExt"],
            "str_cod_expediente": item["strCodExpediente"],
            "id_organizacion_politica": item["idOrganizacionPolitica"],
            "str_organizacion_politica": item["strOrganizacionPolitica"],
            "department": department,
            "str_provincia": item["strProvincia"],
            "str_distrito": item["strDistrito"],
            "str_estado_exped": item["strEstadoExped"],
            "str_tipo_eleccion": item["strTipoEleccion"],
            "id_jurado_electoral": item["idJuradoElectoral"],
            "str_jurado_electoral": item["strJuradoElectoral"],
            "id_tipo_expediente": item["idTipoExpediente"],
            "str_tipo_expediente": item["strTipoExpediente"],
            "id_materia": item["idMateria"],
            "str_materia": item["strMateria"],
        }

        id_expediente = item["idExpediente"]
        obj, created = Expediente.objects.update_or_create(
            id_expediente=id_expediente,
            defaults=defaults,
        )
        if created:
            print(f"created {obj}")


def update_candidates_in_lists():
    """Search our stored Expedientes and search for candidates that we dont have
    in our database
    """
    election = Elections.objects.get(
        name='Elecciones Generales 2021'
    )
    base_url = 'https://plataformaelectoral.jne.gob.pe/Expediente/BuscandoCodigo?strNumExpedienteFiltro='

    created_persons = []

    for exp in Expediente.objects.filter(
        str_materia__icontains='solici'
    ).order_by('id'):
        print(exp.id)
        sleep(0.05)
        url = f"{base_url}{exp.str_cod_expediente_ext}"
        payload = {'strNumExpedienteFiltro': exp.str_cod_expediente_ext}
        res = requests.post(url, data=payload)
        data = res.json().get("data")
        if data:
            for item in data.get("lCandidatosExpediente"):
                idHojaVida = item["idHojaVida"]
                hoja_vida, _ = HojaVida.objects.get_or_create(idHojaVida=idHojaVida)
                dni = item["strDocumentoIdentidad"]
                item.pop("strDocumentoIdentidad")
                item["idHojaVida"] = hoja_vida
                person, created = Person.objects.get_or_create(
                    strDocumentoIdentidad=dni,
                )
                if created:
                    person.elections.add(election)
                    Person.objects.filter(id=person.id).update(**item)
                    person.refresh_from_db()

                    person.idHojaVida = hoja_vida
                    person.dni_number = person.strDocumentoIdentidad
                    person.first_names = person.strNombres
                    person.last_names = f'{person.strApellidoPaterno} {person.strApellidoMaterno}'
                    person.save()
                    print(f'created {person}')
                    created_persons.append(person)

    print(f'created {len(created_persons)} {created_persons}')


def crawl_candidates_in_lists():
    election = Elections.objects.get(
        name='Elecciones Generales 2021'
    )
    base_url = 'https://plataformaelectoral.jne.gob.pe/Expediente/BuscandoCodigo?strNumExpedienteFiltro='

    for exp in Expediente.objects.all():
        url = f"{base_url}{exp.str_cod_expediente_ext}"
        payload = {'strNumExpedienteFiltro': exp.str_cod_expediente_ext}
        res = requests.post(url, data=payload)
        data = res.json().get("data")
        if data:
            for item in data.get("lCandidatosExpediente"):
                idHojaVida = item["idHojaVida"]
                hoja_vida, _ = HojaVida.objects.get_or_create(idHojaVida=idHojaVida)
                dni = item["strDocumentoIdentidad"]
                item.pop("strDocumentoIdentidad")
                item["idHojaVida"] = hoja_vida
                person, created = Person.objects.get_or_create(
                    strDocumentoIdentidad=dni,
                )
                if created:
                    print(f'created {person}')
                    person.elections.add(election)
                Person.objects.filter(id=person.id).update(**item)


def crawl_sentencia_penal():
    base_url = "https://plataformaelectoral.jne.gob.pe/HojaVida/GetAllHVSentenciaPenal?Ids="
    election = Elections.objects.get(name='Elecciones Generales 2021')
    candidates = Person.objects.filter(elections=election)
    candidates_count = candidates.count()

    i = 1
    for candidate in candidates:
        print(f"doing candidate {i}/{candidates_count}")
        i += 1
        id_hoja_de_vida = candidate.idHojaVida.idHojaVida
        url = f"{base_url}{id_hoja_de_vida}-0-ASC"
        res = requests.get(url)
        data = res.json()
        items = data.get("data")

        for item in items:
            if item.get("strTengoSentenciaPenal") == "2":
                continue
            obj_id = item["idHVSentenciaPenal"]
            item.pop("idHVSentenciaPenal")
            item["idHojaVida"] = candidate.idHojaVida
            obj, created = SentenciaPenal.objects.update_or_create(
                idHVSentenciaPenal=obj_id,
                defaults=item,
            )
            obj.person = candidate
            obj.save()

            if created:
                print(f"created {obj}")
            else:
                print(f"updated {obj}")


def crawl_sentencia_obliga():
    base_url = "https://plataformaelectoral.jne.gob.pe/HojaVida/GetAllHVSentenciaObliga?Ids="
    election = Elections.objects.get(name='Elecciones Generales 2021')
    candidates = Person.objects.filter(elections=election)
    candidates_count = candidates.count()

    i = 1
    for candidate in candidates:
        print(f"doing candidate {i}/{candidates_count}")
        i += 1
        id_hoja_de_vida = candidate.idHojaVida.idHojaVida
        url = f"{base_url}{id_hoja_de_vida}-0-ASC"
        res = requests.get(url)
        data = res.json()
        items = data.get("data")

        for item in items:
            if item.get("strTengoSentenciaObliga") == "2":
                continue
            obj_id = item["idHVSentenciaObliga"]
            item.pop("idHVSentenciaObliga")
            item["idHojaVida"] = candidate.idHojaVida
            obj, created = SentenciaObliga.objects.update_or_create(
                idHVSentenciaObliga=obj_id,
                defaults=item,
            )
            obj.person = candidate
            obj.save()

            if created:
                print(f"created {obj}")
            else:
                print(f"updated {obj}")
