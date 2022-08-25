import os
from urllib.parse import urlsplit

import requests
from django.core.management.base import BaseCommand, CommandError
from django.core.management.base import CommandParser

from places.models import Image, Place
from where_to_go import settings


class Command(BaseCommand):
    help = 'Загрузка нового интересного места по ссылке'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('url')

    def handle(self, *args, **options):
        response = requests.get(options['url'])
        response.raise_for_status()

        place_data = response.json()

        title = place_data.get('title')

        if not title:
            raise CommandError('В загружаемом файле нет названия места')
        
        if not place_data.get('coordinates'):
            raise CommandError('В загружаемом файле нет координат места')

        try:
            lat = place_data['coordinates']['lat']
        except KeyError:
            raise CommandError('Широта не указана')

        try:
            lng = place_data['coordinates']['lng']
        except KeyError:
            raise CommandError('Долгота не указана')

        description_short = place_data.get('description_short')
        description_long = place_data.get('description_long')

        place, created = Place.objects.get_or_create(
            title=title,
            latitude=lat,
            longitude=lng
        )

        if created:
            Place.objects.filter(
                title=title,
                latitude=lat,
                longitude=lng
            ).update(
                description_short = description_short,
                description_long = description_long
            )

        for index, img_url in enumerate(place_data.get('imgs'), start=1):
            img_filename = urlsplit(img_url).path.split("/")[-1]

            try:
                response = requests.get(img_url)
                response.raise_for_status()
            except requests.HTTPError:
                continue

            with open(os.path.join(settings.MEDIA_ROOT, img_filename), 'wb') as img_file:
                img_file.write(response.content)

            image = Image.objects.create(
                place=place,
                position=index,
                image=os.path.join(settings.MEDIA_ROOT, img_filename)
            )

        print(f'"{title}" Добавлена в базу данных...')
