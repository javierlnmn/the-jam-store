from django.contrib.auth.models import AbstractUser
from django.db import models

class Direccion(models.Model):
    pais = models.CharField(max_length=255, default='España')
    provincia = models.
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")
    
class CategoriaUsuario(models.Model):
    categoria = models.CharField(max_length=255,) # USUARIO / EMPRESA (son las opciones)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")

class CustomUser(AbstractUser):
    telefono = models.CharField(max_length=20)
    direccion = models.ForeignKey()
    categoria = models.ForeignKey()
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")