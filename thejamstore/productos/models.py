from django.db import models

CATEGORIA_CHOICES = (
    ("superior", "Superior"),
    ("inferior", "Inferior"),
    ("accesorios", "Accesorios"),
    ("zapatillas", "Zapatillas"),
    # Añadir categorias podria alterar el comportamiento del header de la pagina, mejor no añadir demasiadas
)


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, choices=CATEGORIA_CHOICES)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")


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
    categoria_padre = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")


class Talla(models.Model):
    talla = models.CharField(max_length=20)


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    referencia = models.CharField(max_length=255)
    descripcion = models.TextField()
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True, blank=True
    )
    imagen = models.ImageField(verbose_name="foto producto", upload_to="productos")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    oferta = models.BooleanField(null=True)
    precio_oferta = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    talla = models.ManyToManyField(
        Talla, through="ProductoTalla"
    )  # A traves de la talla se sabe si hay o no disponibilidad del producto
    producto_color = models.ManyToManyField(Color)
    producto_marca = models.ManyToManyField(Marca)
    producto_ajuste = models.ManyToManyField(Ajuste)
    producto_tipo_prenda = models.ForeignKey(
        TipoPrenda,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={"categoria_padre": categoria},
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")

    @property
    def hay_stock(self):
        return False

    def __str__(self):
        return self.nombre + ", " + self.referencia + ", " + self.descripcion

    def save(self, *args, **kwargs):
        if not self.categoria:
            raise ValueError("La categoría es obligatoria.")
        super().save(*args, **kwargs)


class ProductoTalla(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    talla = models.ForeignKey(Talla, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)
