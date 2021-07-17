from django.shortcuts import render
from .models import Location

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def location_index(request):
    locations = Location.objects.all()
    return render(request, 'locations/index.html', { 'locations': locations})