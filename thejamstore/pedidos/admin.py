from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from .models import *
from django.core.exceptions import ValidationError


class PedidoProductoFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        productos = []
        for form in self.forms:
            productos.append(
                (form.cleaned_data.get("producto"), form.cleaned_data.get("talla"))
            )
        productos_no_duplicados = set(productos)
        if len(productos_no_duplicados) < len(productos):
            raise ValidationError(
                "Hay productos duplicados. Modifique el producto o seleccione otra talla."
            )


class PedidoProductoInline(admin.TabularInline):
    model = Pedido_Producto
    extra = 1
    formset = PedidoProductoFormSet


class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        "usuario",
        "direccion",
        "codigo_pedido",
        "estado",
        "display_productos_list",
    )
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
