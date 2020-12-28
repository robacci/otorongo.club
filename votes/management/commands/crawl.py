from django.core.management.base import BaseCommand
import requests

from votes.models import Person, Elections, SentenciaPenal, SentenciaObliga


class Command(BaseCommand):
    help = "Crawl candidates from JNE page."

    def add_arguments(self, parser):
        parser.add_argument('-csp', '--crawl_sentencia_penal', action='store_true',
                            help='crawl sentencia penal')
        parser.add_argument('-cso', '--crawl_sentencia_obliga', action='store_true',
                            help='crawl sentencia obliga')

    def handle(self, *args, **options):
        if options.get("crawl_sentencia_penal"):
            crawl_sentencia_penal()
        elif options.get("crawl_sentencia_obliga"):
            crawl_sentencia_obliga()


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
