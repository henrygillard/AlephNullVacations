from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

RATINGS = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
)

REACTION = (
    ("N", "Neutral"),
    ("L", "Like"),
    ("D", "Dislike")
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
        return reverse('detail', kwargs={'location_id': self.id})

class Review(models.Model):
    content = models.CharField(max_length=500)
    rating = models.IntegerField(
        "rating",
        choices=RATINGS,
        default=RATINGS[0][0]
    )
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.content}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'review_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    def __str__(self):
        return f"Photo for location_id: {self.location_id} @{self.url}"

class Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    icon = models.CharField(
        "reaction",
        max_length=1,
        choices=REACTION,
        default=REACTION[0][0]
    )
    
    def __str__(self):
        if self.icon == "L":
            return f"{self.user} liked this"
        elif self.icon == "D":
            return f"{self.user} disliked this"

        return f"{self.user} reacted to {self.review}"