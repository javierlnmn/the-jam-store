from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
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
    
class Carrito_ProductoInline(admin.TabularInline):
    model = Carrito_Productos
    extra = 1


class CarritoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'display_productos_list')
    inlines = [Carrito_ProductoInline]
    
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
