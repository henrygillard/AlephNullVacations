from django.contrib import admin
from .models import Location, Review, Photo

# Register your models here.
admin.site.register(Location)
admin.site.register(Review)
admin.site.register(Photo)