from django.urls import path, include
from .views import indice

urlpatterns = [
    path('', indice, name='indice'),
]