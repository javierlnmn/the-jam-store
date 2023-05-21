from django.contrib import admin
from .models import *

class PedidoAdmin(admin.ModelAdmin):
    readonly_fields=('codigo_pedido',)

admin.site.register(Estado_Pedido)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Pedido_Producto)