from django.urls import path, include
from .views import  busqueda_productos, producto_detalle, seccion_productos, seccion_productos_tipo_prenda

app_name = 'productos'

urlpatterns = [
    path('', busqueda_productos, name='busqueda_productos'),
    path('producto/<int:id_producto>', producto_detalle, name='producto_detalle'),
    path('<str:categoria>/', seccion_productos, name='seccion'),
    # slug convierte los string a minusculas, y convierte los espacios a guiones
    path('<str:categoria>/<slug:tipo_prenda>', seccion_productos_tipo_prenda, name='seccion_tipo_prenda')
]