from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from .models import *
from django.core.exceptions import ValidationError
from django.utils.html import format_html


class PedidoProductoFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        productos = [
            (form.cleaned_data.get("producto"), form.cleaned_data.get("talla"))
            for form in self.forms
            if (form.cleaned_data.get("producto") or form.cleaned_data.get("talla")) and not form.cleaned_data.get("DELETE")
        ]

        if not productos:
            raise ValidationError(
                format_html('<div style="padding: 10px 0;">No se puede crear un pedido sin productos.</div>')
            )
            
        productos_no_duplicados = set(productos)
        if len(productos_no_duplicados) < len(productos):
            raise ValidationError(
               format_html('<div style="padding: 10px 0;">Hay productos duplicados. Modifique el producto o seleccione otra talla.</div>')
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
