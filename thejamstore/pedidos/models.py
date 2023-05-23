from django.db import models
from usuarios.models import Custom_User, Direccion
from productos.models import Producto

import uuid


class Estado_Pedido(models.Model):
    descripcion = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Estado del Pedido"
        verbose_name_plural = "Estados de Pedidos"


class Pedido(models.Model):
    usuario = models.ForeignKey(
        Custom_User, on_delete=models.SET_NULL, null=True, blank=True
    )
    direccion = models.ForeignKey(
        Direccion, on_delete=models.SET_NULL, null=True, blank=True
    )
    codigo_pedido = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="Código del pedido",
    )
    producto = models.ManyToManyField(Producto, through="Pedido_Producto")
    estado = models.ForeignKey(
        Estado_Pedido, on_delete=models.SET_NULL, null=True, blank=True
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    def __str__(self):
        return "Pedido de " + self.usuario.username + ", " + str(self.codigo_pedido)

    def save(self, *args, **kwargs):
        if not self.codigo_pedido:
            self.codigo_pedido = uuid.uuid4()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["codigo_pedido"]


class Pedido_Producto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")

    class Meta:
        verbose_name = "Productos en Pedidos"
        verbose_name_plural = verbose_name
