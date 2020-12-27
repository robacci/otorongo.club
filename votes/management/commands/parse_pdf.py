import glob
import re
import subprocess
from datetime import datetime
from typing import List, Optional, Dict, Any, Tuple

from PIL import Image
from django.core.management import BaseCommand

from votes.models import Person


class Command(BaseCommand):
    help = "Parse a pdf made of images into CSV"

    def add_arguments(self, parser):
        parser.add_argument('-i', '--input', action='store')

    def handle(self, *args, **options):
        input_file = options['input']
        parse(input_file)


def parse(input_file):
    print(f"processing {input_file}")
    cmd = f"pdfimages -j {input_file} a"
    subprocess.call(cmd, shell=True)

    filenames = []
    for item in glob.glob('*jpg'):
        im = Image.open(item)
        width, height = im.size
        top = 0
        bottom = height
        left = 0
        right = 1000
        im1 = im.crop((left, top, right, bottom))
        filename = item.replace('.jpg', '-a.png')
        im1.save(filename)
        filenames.append(filename)

        left = right
        right = 1700
        im2 = im.crop((left, top, right, bottom))
        filename = item.replace('.jpg', '-b.png')
        im2.save(filename)
        filenames.append(filename)

        left = right
        right = width
        im3 = im.crop((left, top, right, bottom))
        filename = item.replace('.jpg', '-c.png')
        im3.save(filename)
        filenames.append(filename)

    for filename in filenames:
        print(filename)
        cmd = f"tesseract {filename} {filename.replace('.png', '')}-"
        subprocess.call(cmd, shell=True)

    files_with_votes = []
    for filename in glob.glob('*txt'):
        with open(filename) as handle:
            text = handle.read()
            if ' +++' in text or ' ---' in text:
                print(f'votes {filename}')
                files_with_votes.append(filename)

    parsed_document = parse_document(files_with_votes)
    for key, value in parsed_document.items():
        if key == 'votes':
            for i in value:
                person, _ = Person.objects.get_or_create(
                    first_names=i['first_names'].upper(),
                    last_names=i['last_names'].upper(),
                )
                print(person)


def parse_document(files_with_votes: List[str]) -> Dict[str, Any]:
    parsed_document = dict()
    parsed_document['votes'] = []

    for filename in files_with_votes:
        with open(filename) as handle:
            lines = handle.readlines()
            out = extract_vote_title(lines)
            if out:
                parsed_document.update(out)
            for line in lines:
                res = extract_congress_person_vote(line)
                if res:
                    parsed_document['votes'].append(res)
    return parsed_document


def extract_vote_title(text_lines: List[str]) -> Optional[Dict[str, Any]]:
    """
    Return {
      'vote_datetime': datetime(2018, 10, 1, 10, 5),
      'vote_projects': [150, 195],  # extracted from 'PROYS. 150 y 195'
      'legislature': 'Legislatura 2019-2020',
    }
    """
    out = dict()

    for idx, line in enumerate(text_lines):
        line = line.strip()
        if line.startswith('VOTACION'):
            out['vote_datetime'] = extract_vote_datetime(line)
        elif 'Legislatura' in line:
            out['legislature'] = extract_legislature(line)
        elif 'Asunto:' in line:
            out['vote_projects'] = extract_vote_projects(text_lines[idx + 1])
    return out


def extract_congress_person_vote(line: str) -> Optional[Dict[str, str]]:
    """

    line: "APP ACUNA NUNEZ, RICHARD aus PPK"
    line: "FLORES VILCHEZ, CLEMENTE SI +++"
    """
    vote = None
    given_names = None

    line = line.strip().split(',')
    if len(line) == 1:
        return None

    valid_last_names = ['VILCATOMA']
    if len(line[0].split(" ")) > 2 and line[0].split(" ")[0] not in valid_last_names:
        # it has political party at start
        last_names = " ".join(line[0].split(" ")[1:])
    else:
        last_names = " ".join(line[0].split(" ")[0:])

    votes = [' aus', ' wae', ' Abst.', ' Lo', ' sinRes', ' LE', ' SinRes']
    if any([line[1].endswith(item) for item in votes]):
        vote = line[1].split(' ')[-1]
        given_names = line[1].replace(vote, '').strip()

    for symbol in ['+++', '---']:
        if symbol in line[1]:
            try:
                idx = line[1].strip().split(' ').index(symbol)
            except ValueError:
                continue
            if symbol == '+++':
                vote = 'SI'
            elif symbol == '---':
                vote = 'NO'
            given_names = " ".join(line[1].strip().split(' ')[:idx - 1])

    if not given_names:
        try:
            given_names = " ".join(line[1].strip().split(" ")[:-2])
        except IndexError:
            return None

    if not vote:
        try:
            vote = line[1].strip().split(' ')[-2]
        except IndexError:
            return None
    return {
        "last_names": last_names,
        "first_names": given_names,
        "vote": vote,
    }


def extract_vote_datetime(line: str) -> Optional[datetime]:
    date_str = re.search(r'.+(\d{2}/\d{2}/\d{4})', line)
    time_str = re.search(r'Hora: (\d{2}:\d{2}) (\w{2})', line)
    if date_str:
        date_str = date_str.group(1)
        time_numbers = time_str.group(1)
        time_am_pm = time_str.group(2)
        date_obj = datetime.strptime(
            f'{date_str} {time_numbers} {time_am_pm}',
            '%d/%m/%Y %I:%M %p',
        )
        return date_obj
    return None


def extract_legislature(line: str) -> Optional[str]:
    return line.strip()


def extract_vote_projects(line: str) -> List[str]:
    """Return list of project ids"""
    return re.findall(r'(\d+)', line)

