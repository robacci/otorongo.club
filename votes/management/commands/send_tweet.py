import random

from django.core.management import BaseCommand
from django.conf import settings

from twitterbot.bot import TwitterBot

from votes.models import Elections, CompiledPerson


class Command(BaseCommand):
    help = "Send tweet about candidate"

    def handle(self, *args, **options):
        election = Elections.objects.get(
            name='Elecciones Generales 2021'
        )
        person_ids = CompiledPerson.objects.filter(
            person__elections=election,
            tweeted=False,
        ).values_list('id', flat=True)
        person_id = random.choice(person_ids)

        compiled_person = CompiledPerson.objects.get(id=person_id)
        tweet(compiled_person)
        compiled_person.tweeted = True
        compiled_person.save()


def tweet(compiled_person):
    twitter = TwitterBot(
        settings.TWITTER_CONSUMER_KEY,
        settings.TWITTER_CONSUMER_SECRET,
        settings.TWITTER_OAUTH_TOKEN,
        settings.TWITTER_OAUTH_TOKEN_SECRET,
    )
    message = (
        f'Candidato(a): {compiled_person.person.last_names} {compiled_person.person.first_names} '
        f'(DNI: {compiled_person.person.dni_number})\n '
        f'{compiled_person.person.strOrganizacionPolitica} \n\n'
        f'Declaró {compiled_person.sentencias_penales} sentencias penales y '
        f'{compiled_person.sentencias_obliga} sentencias de obligaciones. \n\n'
        'Info descargada de la web del JNE.\nVer más en '
        f'https://otorongo.club/2021/candidato/{compiled_person.person.dni_number}/ '
    )
    twitter.tweet_with_photo(message, compiled_person.person.photo.image)
