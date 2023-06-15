from django.urls import path
from .views import pedidos, detalle_pedido, formulario_pago

app_name = 'pedidos'

urlpatterns = [
    path('mis-pedidos/', pedidos, name='pedidos'),
    path('pedido/<int:id_pedido>', detalle_pedido, name='detalle_pedido'),
    path('formulario-pago/', formulario_pago, name='formulario_pago'),
]