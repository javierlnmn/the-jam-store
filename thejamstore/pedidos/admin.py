from django.contrib import admin
from .models import *


class PedidoProductoInline(admin.TabularInline):
    model = Pedido_Producto
    extra = 1


class PedidoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "direccion", "codigo_pedido", "estado", "display_productos_list")
    list_display_links = ("codigo_pedido",)
    readonly_fields = ("codigo_pedido",)
    inlines = [PedidoProductoInline]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related("producto")
        return queryset
    
    def display_productos_list(self, obj):
        productos = obj.producto.all()
        return ", ".join([producto.nombre for producto in productos])

    display_productos_list.short_description = "Productos"

admin.site.register(Estado_Pedido)
admin.site.register(Pedido, PedidoAdmin)
