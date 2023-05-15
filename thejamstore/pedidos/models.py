from django.db import models


# Caracteristicas de los pedidos
class Pedido(models.Model):
    # usuario = models.ForeignKey(Users, on_delete=models.CASCADE)
    # direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    fk_nombre_usuario = models.CharField(max_length=255)
    # productos = models.ManyToManyField(Producto, through='PedidoProducto')
    estado = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")

class PedidoProducto(models.Model):
    # pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    # producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")
