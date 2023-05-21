from django.contrib import admin
from .models import *
from django.utils.html import format_html

class ColorAdmin(admin.ModelAdmin):
    list_display = ('display_color', 'descripcion', 'created', 'updated')
    
    def display_color(self, obj):
        return format_html(
            '<div style="background-color: {}; width: 1rem; height: 1rem;">&nbsp;</div>',
            obj.codigo_hex
        )
    display_color.short_description = 'Color'
    
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('display_imagen', 'nombre')
    list_filter = ('categoria',)
    
    def display_imagen(self, obj):
        return format_html(
            '<img src="{}" style="width: 8rem; height: 8rem; max-width: 100%; height: auto;">',
            obj.imagen.url
        )
    
        
    display_imagen.short_description = 'Vista previa'


admin.site.register(Categoria)
admin.site.register(Color, ColorAdmin)
admin.site.register(Marca)
admin.site.register(Ajuste)
admin.site.register(Tipo_Prenda)
admin.site.register(Talla)
admin.site.register(Producto, ProductoAdmin)
