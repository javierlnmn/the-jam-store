from django.contrib import admin
from .models import *

admin.site.register(CategoriaUsuario)
admin.site.register(CustomUser)
admin.site.register(Direccion)
admin.site.register(Carrito)
admin.site.register(CarritoProductos)
admin.site.register(ListaDeseos)
admin.site.register(Comentario)