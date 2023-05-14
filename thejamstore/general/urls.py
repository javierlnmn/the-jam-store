from django.urls import path, include
from .views import *

urlpatterns = [
    path('', IndiceView.as_view(), name='indice'),
]