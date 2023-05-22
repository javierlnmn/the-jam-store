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
        'is_staff',
        'is_superuser',
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'telefono')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

class Carrito_ProductosAdmin(admin.ModelAdmin):
    list_display = (
        'producto',
        'cantidad',
        'carrito'
    )

admin.site.register(Categoria_Usuario)
admin.site.register(Custom_User, Custom_UserAdmin)
admin.site.register(Direccion)
admin.site.register(Carrito)
admin.site.register(Carrito_Productos, Carrito_ProductosAdmin)
admin.site.register(Lista_Deseos)
admin.site.register(Comentario)
admin.site.register(Peticiones)
