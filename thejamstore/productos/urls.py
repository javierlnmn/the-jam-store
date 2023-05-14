from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ProductoView.as_view(), name='indice'),
]