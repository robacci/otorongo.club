from time import sleep
import requests

from django.core.management import BaseCommand
from parsel import Selector

from votes.models import Person


class Command(BaseCommand):
    help = "Search DNIs of person"

    def handle(self, *args, **options):
        search()


def search():
    # search_voto_informado()
    search_infogob()


def search_infogob():
    base_url = "https://infogob.jne.gob.pe"

    res = requests.get(base_url + '/Politico')
    sel = Selector(res.text)
    token = sel.xpath('//input[@id="key"]/@value').extract_first()

    persons = Person.objects.filter(dni_number__isnull=True)
    out = []

    for person in persons:
        sleep(3)
        print(f'\n\nsearching {person}')
        payload = {
            "IdDNI": "",
            "TxApePat": person.last_names.lower().split(' ')[0],
            "TxApeMat": person.last_names.lower().split(' ')[-1],
            "TxNombre": person.first_names.lower(),
            "token": token,
        }
        res = requests.post(base_url + '/Politico/ListarPolitico', data=payload)
        res_json = res.json()

        try:
            results = res_json['Data']
            print(f'found {person}')
        except (TypeError, KeyError):
            continue

        for result in results:
            sleep(3)
            url = base_url + result['TxRutaPolitico']
            out.append((person, url))

    for i in out:
        print(i)


def search_voto_informado():
    base_url = "https://votoinformado.jne.gob.pe/voto/Home/CargarBusquedaCandidatos"
    persons = Person.objects.filter(dni_number__isnull=True)

    out = []

    for person in persons:
        print(f'\n\nsearching {person}')
        payload = {
            "TXUBIGEO": "000000",
            "TXNOMBRES": person.first_names.lower().split(' ')[0],
            "TXAPELLIDOS": " ".join(person.last_names.lower().split(' ')[:2]),
        }
        res = requests.post(base_url, data=payload)
        res_json = res.json()
        try:
            results = res_json['data']['Data']
            print(f'Found {person}')
        except (TypeError, KeyError):
            continue

        sleep(3)

        for result in results:
            crypted_id = result['IDENCRIPTADO']
            dni = fetch_dni_voto_informado(crypted_id)
            if dni:
                out.append((person, dni))
                print(f'Found dni {dni}')

        sleep(5)

    for i in out:
        print(i)


def fetch_dni_voto_informado(crypted_id):
    base_url = "https://votoinformado.jne.gob.pe/voto/HojaVida/CargarHojaVida"
    payload = {
        'TxCodigo': crypted_id
    }
    res = requests.post(base_url, data=payload)
    res_json = res.json()

    try:
        dni = res_json['data']['Data']['TXDOCUMENTOIDENTIDAD']
    except KeyError:
        return

    return dni

