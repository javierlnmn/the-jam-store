from django.urls import path, include
from .views import indice

app_name = 'general'

urlpatterns = [
    path('', indice, name='indice'),
]