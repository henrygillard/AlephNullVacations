from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)


