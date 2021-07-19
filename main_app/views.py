from django.db.models.aggregates import Avg
from django.shortcuts import render, redirect
from .models import Location, Review
from .forms import ReviewForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


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
    return render(request, 'locations/index.html', {'locations': locations})


def location_detail(request, location_id):
    location = Location.objects.get(id=location_id)
    review_form = ReviewForm()
    total = 0
    if len(location.review_set.all()):
        for review in location.review_set.all():
            if review.rating == "1":
                total += 1
            elif review.rating == "2":
                total += 2
            elif review.rating == "3":
                total += 3
            elif review.rating == "4":
                total += 4
            elif review.rating == "5":
                total += 5
        total = total * 100 / len(location.review_set.all())
        total = round(total)
        total = total / 100
    if not total:
        average = f"{total} / 5"
    else:
        average = f"No Reviews"

    return render(request, 'locations/detail.html', {
        'location': location,
        'review_form': review_form,
        'average': average
    })


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
    success_url = '/'


def add_review(request, location_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.location_id = location_id
        new_review.save()
    return redirect('detail', location_id=location_id)


class ReviewUpdate(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ['content', 'rating']

    def get_success_url(self):
        obj = self.get_object()
        print(obj)
        return reverse('detail', kwargs={'location_id': obj.location.id})


class ReviewDelete(LoginRequiredMixin, DeleteView):
    model = Review

    def get_success_url(self):
        obj = self.get_object()
        print(obj)
        return reverse('detail', kwargs={'location_id': obj.location.id})
