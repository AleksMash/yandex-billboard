from django.db import models
from tinymce.models import HTMLField

# Create your models he

class Place(models.Model):
    title = models.CharField(max_length=100)
    description_short = models.CharField(max_length=350)
    description_long = HTMLField(default='', blank=True)
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(verbose_name='Картинка')
    position = models.IntegerField(default=0, verbose_name='Позиция',
                                   null=False, blank=False, db_index=True)
    place = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'{self.position} {self.place.title}'
