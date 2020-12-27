import datetime

from django.test import TestCase

from votes.management.commands.parse_pdf import extract_vote_title, extract_congress_person_vote


class TestParsePdf(TestCase):
    def test_extract_vote_title(self):
        input = [
            "co",
            "Segunda Legislatura Ordinaria 2017-2018",
            "Sesion del: 17 de Mayo de 2018",
            "VOTACION: Fecha: 17/05/2018 Hora: 01:30 pm",
            "Asunto:",
            "PROYS. 31 Y 120; LEY QUE REGULA LA EJECUCION",
            "APP ACUNA NUNEZ, RICHARD aus PPK",
            "GPFP AGUILAR MONTENEGRO, WILMER SI +++ FA",
            "GPFP ALBRECHT RODRIGUEZ, VICTOR aus NA",
            "GPFP ALCALA MATEO, PERCY SI +++ GPFP",
            "GPFP ALCORTA SUERO, LOURDES SI +++ NA",
            "GPFP ANANCULI GOMEZ, BETTY SI +++ AP",
            "GPFP ANDRADE SALGUERO DE A., GLADYS SI +++ NA",
        ]
        result = extract_vote_title(input)
        expected = {
            'legislature': 'Segunda Legislatura Ordinaria 2017-2018',
            'vote_datetime': datetime.datetime(2018, 5, 17, 13, 30),
            'vote_projects': ['31', '120'],
        }
        self.assertEqual(expected, result)

    def test_extract_congress_person_vote(self):
        input = "APP ACUNA NUNEZ, RICHARD aus PPK"
        expected = (
            "ACUNA NUNEZ, RICHARD",
            "aus"
        )
        result = extract_congress_person_vote(input)
        self.assertEqual(expected, result)

    def test_extract_congress_person_vote__no_party(self):
        input = "FLORES VILCHEZ, CLEMENTE SI +++"
        expected = (
            "FLORES VILCHEZ, CLEMENTE",
            "SI"
        )
        result = extract_congress_person_vote(input)
        self.assertEqual(expected, result)

    def test_extract_congress_person_vote2(self):
        items = [
            {
                "input": "VILLAVICENCIO CARDENAS, FRANCISCO SinRes",
                "expected": ("VILLAVICENCIO CARDENAS, FRANCISCO", "SinRes"),
            },
            {
                "input": "GPFP FIGUEROA MINAYA, MODESTO SI +++ GPFP",
                "expected": ("FIGUEROA MINAYA, MODESTO", "SI"),
            },
            {
                "input": "VILCATOMA DE LA CRUZ, YENI LE",
                "expected": ("VILCATOMA DE LA CRUZ, YENI", "LE"),
            },
            {
                "input": "HERESI CHICOMA, SALVADOR Lo",
                "expected": ("HERESI CHICOMA, SALVADOR", "Lo"),
            },
            {
                "input": "GALARRETA VELARDE, LUIS wae",
                "expected": ("GALARRETA VELARDE, LUIS", "wae"),
            },
            {
                'input': "FUJIMORI HIGUCHI, KENJI GERARDO aus",
                'expected': ("FUJIMORI HIGUCHI, KENJI GERARDO", "aus"),
            },
        ]
        for item in items:
            result = extract_congress_person_vote(item['input'])
            expected = item['expected']
            self.assertEqual(expected, result)

