from django.urls import path
from .views import iniciar_sesion, cerrar_sesion, registrar_usuario

app_name = 'usuarios'

urlpatterns = [
    path('iniciar-sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('cerrar-sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('registrar_usuario/', registrar_usuario, name='registro'),
]