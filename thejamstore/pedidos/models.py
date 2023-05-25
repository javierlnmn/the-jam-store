from django.db import models
from usuarios.models import Custom_User, Direccion
from productos.models import Producto, Talla, Producto_Talla
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db.models import Count

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
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    codigo_pedido = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="Código del pedido",
    )
    producto = models.ManyToManyField(
        Producto,
        through="Pedido_Producto",
    )
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

    def clean(self):
        if not self.estado:
            raise ValidationError({"estado": "Este campo es olbigatorio"})

        if self:
            if self.direccion.usuario != self.usuario:
                raise ValidationError(
                    {
                        "direccion": "La dirección seleccionada no pertenece al usuario seleccionado"
                    }
                )

    class Meta:
        ordering = ["usuario"]


class Pedido_Producto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=False)
    cantidad = models.PositiveIntegerField(
        null=False,
        validators=[MinValueValidator(1)],
    )
    talla = models.ForeignKey(Talla, on_delete=models.CASCADE, null=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")

    def clean(self):
        try:
            producto = Producto.objects.get(pk=self.producto.id)
            inventario_tallas = Producto_Talla.objects.filter(producto=producto.id)
        except:
            raise ValidationError("")

        if not self.producto or not self.cantidad or not self.talla_id:
            raise ValidationError("")

        talla_valida = False
        cantidad_valida = False

        for inventario in inventario_tallas:
            if self.talla == inventario.talla:
                talla_valida = True

                if self.cantidad <= inventario.cantidad:
                    cantidad_valida = True

                break

        if not talla_valida:
            raise ValidationError(
                {"talla": "No disponemos de esta talla en el inventario"}
            )

        if not cantidad_valida:
            raise ValidationError(
                {"cantidad": "No disponemos de esta cantidad en el inventario"}
            )

    class Meta:
        verbose_name = "Productos del pedido"
        verbose_name_plural = "Productos del pedido"
