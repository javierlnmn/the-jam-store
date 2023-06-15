from django.urls import path
from .views import pedidos

app_name = 'pedidos'

urlpatterns = [
    path('mis-pedidos/', pedidos, name='pedidos'),
]