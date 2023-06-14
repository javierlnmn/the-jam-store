from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms.models import BaseInlineFormSet
from django.utils.html import format_html
from .models import *


class Custom_UserAdmin(UserAdmin):
    list_display = (
        "username",
        "categoria",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_superuser",
    )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Información personal", {"fields": ("first_name", "last_name", "foto_perfil", "email", "telefono")}),
        (
            "Permisos",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Fechas de registro", {"fields": ("last_login", "date_joined")}),
    )


class DireccionAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "usuario",
        "provincia",
        "municipio",
        "cod_postal",
        "calle",
        "numero",
    )
    
class CarritoProductoFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        productos = [
            (form.cleaned_data.get("producto"), form.cleaned_data.get("talla"))
            for form in self.forms
            if (form.cleaned_data.get("producto") or form.cleaned_data.get("talla")) and not form.cleaned_data.get("DELETE")
        ]

        if not productos:
            raise ValidationError(
                format_html('<div style="padding: 10px 0;">No se puede crear un carrito sin productos.</div>')
            )
            
        productos_no_duplicados = set(productos)
        if len(productos_no_duplicados) < len(productos):
            raise ValidationError(
               format_html('<div style="padding: 10px 0;">Hay productos duplicados. Modifique el producto o seleccione otra talla.</div>')
            )
    
class CarritoProductoInline(admin.TabularInline):
    model = Carrito_Productos
    extra = 1
    formset = CarritoProductoFormSet


class CarritoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'display_productos_list')
    inlines = [CarritoProductoInline]
    
    def display_productos_list(self, obj):
        productos = obj.producto.all()
        return ", ".join([producto.nombre for producto in productos])
    display_productos_list.short_description = "Productos del carrito"

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("display_comentario", "usuario", "producto", "valoracion")

    def display_comentario(self, obj):
        return (obj.comentario[:90] + '...') if len(obj.comentario) > 90 else obj.comentario
    
class PeticionesAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'usuario', 'precio_display', 'talla')
    
    def precio_display(self, obj):
        return str(obj.precio) + '€'
    precio_display.short_description = "Precio solicitado"


admin.site.register(Categoria_Usuario)
admin.site.register(Custom_User, Custom_UserAdmin)
admin.site.register(Direccion, DireccionAdmin)
admin.site.register(Carrito, CarritoAdmin)
admin.site.register(Lista_Deseos)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Peticiones, PeticionesAdmin)
