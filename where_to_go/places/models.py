from django.db import models

# Create your models he

class Place(models.Model):
    title = models.CharField(max_length=100)
    description_short = models.CharField(max_length=350)
    description_long = models.TextField(blank=True, default='')
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.title