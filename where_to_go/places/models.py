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

class Image(models.Model):
    image = models.ImageField(upload_to='uploads/')
    position = models.IntegerField(default=0)
    place = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.position} {self.place.title}'
