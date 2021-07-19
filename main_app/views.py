from django.shortcuts import render, redirect
from .models import Location
from .forms import ReviewForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


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

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def location_index(request):
    locations = Location.objects.all()
    return render(request, 'locations/index.html', { 'locations': locations})

def location_detail(request, location_id):
  location = Location.objects.get(id=location_id)
  print(location)
  review_form = ReviewForm()

  return render(request, 'locations/detail.html', { 
      'location':location,
      'review_form': review_form
       })

def add_review(request, location_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.location_id = location_id
        new_review.save()
    return redirect('detail', location_id=location_id)



class LocationCreate(LoginRequiredMixin, CreateView):
  model = Location
  fields = ['name', 'country', 'city', 'latitude', 'longitude']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class LocationUpdate(LoginRequiredMixin, UpdateView):
  model = Location
  fields = ['name', 'country', 'city', 'latitude', 'longitude']

class LocationDelete(LoginRequiredMixin, DeleteView):
  model = Location
  success_url = '/locations/'