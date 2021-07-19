from django.urls import path, include
from . import views

urlpatterns = [
    #NAV PATHS
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('locations/', views.location_index, name='index'),
    path('locations/<int:location_id>/', views.location_detail, name='detail'),
    #USER PATHS
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    #CRUD LOCATIONS
    path('locations/create/', views.LocationCreate.as_view(), name='locations_create'),
    path('locations/<int:pk>/update/', views.LocationUpdate.as_view(), name='locations_update'),
    path('locations/<int:pk>/delete/', views.LocationDelete.as_view(), name='locations_delete'),
    #CRUD REVIEWS
    path('locations/<int:location_id>/add_review/', views.add_review, name='add_review'),
    path('locations/<int:pk>/delete_review/', views.ReviewDelete.as_view(), name='delete_review'),
    path('locations/<int:pk>/update_review/', views.ReviewUpdate.as_view(), name='update_review'),
    #CRUD PHOTOS
    path('locations/<int:location_id>/add_photo/', views.add_photo, name='add_photo'),
    

]