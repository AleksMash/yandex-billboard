from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование локации')
    description_short = models.TextField(blank=True, verbose_name='Краткое описание')
    description_long = HTMLField(blank=True, verbose_name='Полное описание')
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(verbose_name='Картинка')
    position = models.IntegerField(default=0, verbose_name='Позиция', db_index=True)
    place = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'{self.position} {self.place.title}'
