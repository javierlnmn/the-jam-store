from django.urls import path, include
from .views import iniciar_sesion, cerrar_sesion

app_name = 'usuarios'

urlpatterns = [
    path('iniciar-sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('cerrar-sesion/', cerrar_sesion, name='cerrar_sesion'),
]