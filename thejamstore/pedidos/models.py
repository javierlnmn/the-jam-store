from django.db import models
from usuarios.models import CustomUser, Direccion
from productos.models import Producto


class Pedido(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    direccion = models.ForeignKey(Direccion, on_delete=models.SET_NULL, null=True, blank=True)
    producto = models.ManyToManyField(Producto, through="PedidoProducto")
    estado = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    
    def save(self, *args, **kwargs):
        if not self.usuario or not self.direccion:
            raise ValueError("La dirección o el usuario son obligatorios.")
        super().save(*args, **kwargs)


class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")
