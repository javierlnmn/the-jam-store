from django.contrib import admin
from .models import *
from django.utils.html import format_html


class ColorAdmin(admin.ModelAdmin):
    list_display = ("display_color", "descripcion")
    list_display_links = ("display_color", "descripcion")

    def display_color(self, obj):
        return format_html(
            '<div style="background-color: {}; width: 5rem; height: 1rem;">&nbsp;</div>',
            obj.codigo_hex,
        )

    display_color.short_description = "Color"


class Tipo_PrendaAdmin(admin.ModelAdmin):
    list_display = ("descripcion", "categoria_padre")
    list_filter = ("categoria_padre",)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ("display_imagen", "nombre", "referencia", "display_hay_stock")
    list_display_links = ("display_imagen", "nombre")
    list_filter = ("categoria",)

    def display_imagen(self, obj):
        return format_html(
            '<img src="{}" style="width: 8rem; height: 8rem; max-width: 100%; height: auto; aspect-ratio: 1; object-fit: cover;">',
            obj.imagen.url,
        )

    display_imagen.short_description = "Vista previa"

    def display_hay_stock(self, obj):
        return obj.get_stock

    display_hay_stock.boolean = True
    display_hay_stock.short_description = "Hay Stock"


class Producto_TallaAdmin(admin.ModelAdmin):
    list_display = ("display_imagen", "producto", "talla", "cantidad")
    list_filter = ("talla",)


    def display_imagen(self, obj):
        return format_html(
            '<img src="{}" style="width: 8rem; height: 8rem; max-width: 100%; height: auto;">',
            obj.producto.imagen.url,
        )

    display_imagen.short_description = "Vista previa"


admin.site.register(Categoria)
admin.site.register(Color, ColorAdmin)
admin.site.register(Marca)
admin.site.register(Ajuste)
admin.site.register(Tipo_Prenda, Tipo_PrendaAdmin)
admin.site.register(Talla)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Producto_Talla, Producto_TallaAdmin)
admin.site.register(Producto_Destacado)
