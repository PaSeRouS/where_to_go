from urllib.parse import urlsplit
from io import BytesIO

import requests
from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand, CommandError, CommandParser

from places.models import Place


class Command(BaseCommand):
    help = 'Загрузка нового интересного места по ссылке'


    def add_arguments(self, parser: CommandParser):
        parser.add_argument('url')

    
    def handle(self, *args, **options):
        response = requests.get(options['url'])
        response.raise_for_status()

        place_data = response.json()

        title = place_data.get('title')
        lat = float(place_data['coordinates']['lat'])
        lng = float(place_data['coordinates']['lng'])
        description_short = place_data.get('description_short')
        description_long = place_data.get('description_long')

        new_place, created = Place.objects.get_or_create(
            title=title,
            description_short=description_short,
            description_long=description_long,
            latitude=lat,
            longitude=lng,
        )

        for index, img_url in enumerate(place_data.get('imgs')):
            img_filename = urlsplit(img_url).path.split("/")[-1]

            try:
                response = requests.get(img_url)
                response.raise_for_status()
            except requests.HTTPError as err:
                continue

            img_file = ImageFile(BytesIO(response.content))

            new_image = new_place.images.create()
            new_image.image.save(img_filename, img_file, save=False)
            new_image.image_id = index + 1
            new_image.save()

        print(f'"{title}" Добавлена в базу данных...')