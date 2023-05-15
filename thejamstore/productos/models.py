from django.db import models


# Caracteristicas de los productos
class Color(models.Model):
    descripcion = models.CharField(max_length=255)
    codigo_hex = models.CharField(max_length=7)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")


class Marca(models.Model):
    descripcion = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")


class Ajuste(models.Model):
    descripcion = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")


class TipoPrenda(models.Model):
    descripcion = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    referencia = models.CharField(max_length=255)
    descripcion = models.TextField()
    imagen = models.ImageField(verbose_name="foto producto", upload_to="productos")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    oferta = models.BooleanField(null=True)
    precio_oferta = models.DecimalField(max_digits=10, decimal_places=2)
    talla_xs = models.IntegerField(default=0)
    talla_s = models.IntegerField(default=0)
    talla_m = models.IntegerField(default=0)
    talla_l = models.IntegerField(default=0)
    talla_xl = models.IntegerField(default=0)
    producto_color = models.ManyToManyField(Color)
    producto_marca = models.ManyToManyField(Marca)
    producto_ajuste = models.ManyToManyField(Ajuste)
    producto_tipo_prenda = models.ManyToManyField(TipoPrenda)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")

    def __str__(self):
        return self.nombre + ", " + self.referencia + ", " + self.descripcion

    @property
    def hay_stock(self):
        total_productos = (
            self.talla_xs + self.talla_s + self.talla_m + self.talla_l + self.talla_xl
        )
        if total_productos > 0:
            return True
        return False


class PuntuacionValoracion(models.IntegerChoices):
    MUY_MALO = 1, "Muy malo"
    MALO = 2, "Malo"
    ACEPTABLE = 3, "Aceptable"
    BUENO = 4, "Bueno"
    EXCELENTE = 5, "Excelente"


class Comentario(models.Model):
    comentario = models.TextField()
    valoracion = models.IntegerChoices(choices=PuntuacionValoracion.choices)
    # usuario = models.ForeignKey(Users, on_delete=models.CASCADE)
    # producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")
