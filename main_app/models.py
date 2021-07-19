from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

RATINGS = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),

)

class Location(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('location_detail', kwargs={'location_id': self.id})

    def get_absolute_url(self):
        return reverse('detail', kwargs={'location_id': self.id})

class Review(models.Model):
    content = models.CharField(max_length=500)
    rating = models.CharField(
        "rating",
        max_length=1,
        choices=RATINGS,
        default=RATINGS[0][0]
    )
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.content}"