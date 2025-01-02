from django.urls import path
from .views import *



urlpatterns = [
    path('', home, name='home'),  # Corrected to use the 'home' view directly
]