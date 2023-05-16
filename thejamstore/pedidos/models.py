from django.db import models
from usuarios.models import Custom_User, Direccion
from productos.models import Producto


class Estado_Pedido(models.Model):
    descripcion = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")

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
    producto = models.ManyToManyField(Producto, through="Pedido_Producto")
    estado = models.ForeignKey(Estado_Pedido, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")

    def save(self, *args, **kwargs):
        if not self.usuario or not self.direccion or not self.estado:
            raise ValueError("Hay que rellenar los campos obligatorios.")
        super().save(*args, **kwargs)


class Pedido_Producto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")

    class Meta:
        verbose_name = "Productos en Pedidos"
        verbose_name_plural = verbose_name
