from django.urls import path, include
from .views import *

app_name = 'general'

urlpatterns = [
    path('', IndiceView.as_view(), name='indice'),
]