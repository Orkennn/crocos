from django.db import models

# Create your models here.

from django.db import models


class Landmark(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    photo = models.ImageField(upload_to='landmark_photos/')

    def __str__(self):
        return self.name
