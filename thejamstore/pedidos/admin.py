from django.contrib import admin
from .models import *


class PedidoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "direccion", "codigo_pedido", "estado")
    readonly_fields = ("codigo_pedido",)
    
class Pedido_ProductoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'producto', 'cantidad')


admin.site.register(Estado_Pedido)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Pedido_Producto, Pedido_ProductoAdmin)
