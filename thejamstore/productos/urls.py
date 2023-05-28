from django.urls import path, include
from .views import producto_detalle, seccion_productos

app_name = 'productos'

urlpatterns = [
    path('producto/<int:id_producto>', producto_detalle, name='producto_detalle'),
    path('<str:categoria>/', seccion_productos, name='seccion'),
]