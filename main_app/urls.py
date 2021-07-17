from django.urls import path, include
from . import views

urlpatterns = [
    #NAV PATHS
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('locations/', views.location_index, name='index'),
    #USER PATHS
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    #Details Path
    path('locations/<int:location_id>/', views.location_detail, name='detail'),
]