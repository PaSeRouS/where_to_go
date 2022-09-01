import os
from io import BytesIO
from urllib.parse import urlsplit

import requests
from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand, CommandError
from django.core.management.base import CommandParser

from places.models import Image, Place
from where_to_go import settings


def get_or_create_place(place_data):
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
    if not description_short:
        description_short = 'Краткое описание отсутствует'

    description_long = place_data.get('description_long')
    if not description_long:
        description_long = 'Подробное описание отсутствует'

    place, created = Place.objects.get_or_create(
        title=title,
        defaults={
            'latitude': lat,
            'longitude': lng,
            'description_short': description_short,
            'description_long': description_long
        }
    )

    return place, title


def add_image_to_place(place, index, img_url):
    img_filename = urlsplit(img_url).path.split("/")[-1]

    try:
        response = requests.get(img_url)
        response.raise_for_status()

        img_file = ImageFile(BytesIO(response.content))

        image = Image.objects.create(
            place=place,
            position=index
        )

        image.image.save(img_filename, img_file)
    except requests.HTTPError:
        pass


class Command(BaseCommand):
    help = 'Загрузка нового интересного места по ссылке'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('url')


    def handle(self, *args, **options):
        response = requests.get(options['url'])
        response.raise_for_status()

        place_data = response.json()
        place, title = get_or_create_place(place_data)

        for index, img_url in enumerate(place_data.get('imgs'), start=1):
            add_image_to_place(place, index, img_url)

        print(f'"{title}" Добавлена в базу данных...')
