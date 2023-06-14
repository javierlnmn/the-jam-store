from django.urls import path
from .views import iniciar_sesion, cerrar_sesion, registrar_usuario, valorar_producto, lista_deseos, anadir_a_lista_deseos, quitar_de_lista_deseos, carrito, anadir_a_carrito, actualizar_datos_usuario, ver_direcciones, formulario_crear_direccion, anadir_direccion, eliminar_direccion, formulario_editar_direccion, editar_direccion

app_name = 'usuarios'

urlpatterns = [
    path('iniciar-sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('cerrar-sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('registro/', registrar_usuario, name='registrar_usuario'),
    path('actualizar/', actualizar_datos_usuario, name='actualizar_datos_usuario'),
    
    path('valorar/<int:id_producto>', valorar_producto, name='valorar_producto'),
    
    path('lista-de-deseos/', lista_deseos, name='lista_deseos'),
    path('anadir-a-lista-deseos/<int:id_producto>', anadir_a_lista_deseos, name='anadir_a_lista_deseos'),
    path('quitar-de-lista-deseos/<int:id_producto>', quitar_de_lista_deseos, name='quitar_de_lista_deseos'),
    
    path('carrito/', carrito, name='carrito'),
    path('anadir_a_carrito/<int:id_producto>', anadir_a_carrito, name='anadir_a_carrito'),
    
    path('direcciones/', ver_direcciones, name='ver_direcciones'),
    path('direcciones/formulario-crear-direccion/', formulario_crear_direccion, name='formulario_crear_direccion'),
    path('direcciones/anadir-direccion/', anadir_direccion, name='anadir_direccion'),
    path('direcciones/eliminar-direccion/<int:id_direccion>', eliminar_direccion, name='eliminar_direccion'),
    path('direcciones/formulario-editar-direccion/<int:id_direccion>', formulario_editar_direccion, name='formulario_editar_direccion'),
    path('direcciones/editar-direccion/<int:id_direccion>', editar_direccion, name='editar_direccion'),
]