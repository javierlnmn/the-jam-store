from django.urls import path
from .views import iniciar_sesion, cerrar_sesion, registrar_usuario, valorar_producto, lista_deseos, anadir_a_lista_deseos, quitar_de_lista_deseos,actualizar_datos_usuario, ver_direcciones

app_name = 'usuarios'

urlpatterns = [
    path('iniciar-sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('cerrar-sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('registro/', registrar_usuario, name='registrar_usuario'),
    path('actualizar/', actualizar_datos_usuario, name="actualizar_datos_usuario"),
    path('valorar/<int:id_producto>', valorar_producto, name='valorar_producto'),
    path('anadir-a-lista-deseos/<int:id_producto>', anadir_a_lista_deseos, name='anadir_a_lista_deseos'),
    path('quitar-de-lista-deseos/<int:id_producto>', quitar_de_lista_deseos, name='quitar_de_lista_deseos'),
    path('lista-de-deseos/', lista_deseos, name='lista_deseos'),
    path('direcciones/', ver_direcciones, name='ver_direcciones')
]