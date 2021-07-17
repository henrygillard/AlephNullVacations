from django.shortcuts import render, redirect
from .models import Location
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def location_index(request):
    locations = Location.objects.all()
    return render(request, 'locations/index.html', { 'locations': locations})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)