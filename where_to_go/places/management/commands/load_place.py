import os
from urllib.parse import urlparse

import requests

from django.core.management.base import BaseCommand, CommandError
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
        place, created = Place.objects.get_or_create(title=place_serialized['title'])
        if created:
            place.title = place_serialized['title']
            for num, img_url in enumerate(place_serialized['imgs'], 1):
                print(f'Скачиваем картинку {num}')
                response = requests.get(img_url)
                try:
                    response.raise_for_status()
                except Exception:
                    pass
                else:
                    file = ContentFile(response.content)
                    image = Image.objects.create(place=place)
                    file_name = os.path.basename(urlparse(img_url).path)
                    image.image.save(file_name, file, True)
                    place.images.add(image)
            place.description_short = place_serialized['description_short']
            place.description_long = place_serialized['description_long']
            place.lng = place_serialized['coordinates']['lng']
            place.lat = place_serialized['coordinates']['lat']
            place.save()
            self.stdout.write(self.style.SUCCESS('Место добавлено'))