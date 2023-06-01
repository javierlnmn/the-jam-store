from django.urls import path
from .views import iniciar_sesion, cerrar_sesion, registrar_usuario, valorar_producto

app_name = 'usuarios'

urlpatterns = [
    path('iniciar-sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('cerrar-sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('registro/', registrar_usuario, name='registrar_usuario'),
    path('valorar/<int:id_producto>', valorar_producto, name='valorar_producto')
]