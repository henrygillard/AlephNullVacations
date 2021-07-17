from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('location_detail', kwargs={'location_id': self.id})
