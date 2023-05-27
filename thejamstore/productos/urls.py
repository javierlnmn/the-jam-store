from django.urls import path, include
from .views import producto_detalle

app_name = 'productos'

urlpatterns = [
    path('producto/<int:id_producto>', producto_detalle, name='producto_detalle'),
]