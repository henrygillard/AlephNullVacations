from django.contrib import admin
from .models import Location, Review, Photo, Reaction

# Register your models here.
admin.site.register(Location)
admin.site.register(Review)
admin.site.register(Photo)
admin.site.register(Reaction)