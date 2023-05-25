import os
from urllib.parse import urlparse

import requests

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile


from places.models import Place, Image


class Command(BaseCommand):
    help = 'Load place data from GeoJson files'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)

    def handle(self, *args, **options):
        url = options['url']
        response = requests.get(url)
        response.raise_for_status()
        place_serialized = response.json()
        defaults = {
            'description_short': place_serialized.get('description_short'),
            'description_long': place_serialized.get('description_long'),
            'lng': place_serialized['coordinates']['lng'],
            'lat': place_serialized['coordinates']['lat']
        }
        place, created = Place.objects.get_or_create(title=place_serialized['title'],
                                                     defaults=defaults)
        if not created:
            self.stdout.write(self.style.SUCCESS('Данное место уже есть в базе данных'))
            return

        self.stdout.write(self.style.SUCCESS('Скачиваем изображения...'))
        images = place_serialized.get('imgs', [])

        for num, img_url in enumerate(images, 1):
            response = requests.get(img_url)
            response.raise_for_status()
            file = ContentFile(response.content, name=os.path.basename(urlparse(img_url).path))
            Image.objects.create(place=place, image=file)

        self.stdout.write(self.style.SUCCESS('Место добавлено в базу данных'))

