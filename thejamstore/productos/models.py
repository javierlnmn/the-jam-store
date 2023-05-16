from django.db import models
from django.core.exceptions import ValidationError

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

    def __str__(self):
        return self.nombre


# Caracteristicas de los productos
class Color(models.Model):
    descripcion = models.CharField(max_length=255)
    codigo_hex = models.CharField(max_length=7)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colores"


class Marca(models.Model):
    descripcion = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")

    def __str__(self):
        return self.descripcion


class Ajuste(models.Model):
    descripcion = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Ajuste de la Prenda"
        verbose_name_plural = "Ajuste de la Prenda"


class Tipo_Prenda(models.Model):
    descripcion = models.CharField(max_length=255)
    categoria_padre = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Tipo de Prenda"
        verbose_name_plural = "Tipos de Prenda"


class Talla(models.Model):
    talla = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    referencia = models.CharField(max_length=255)
    descripcion = models.TextField()
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True, blank=True
    )
    imagen = models.ImageField(verbose_name="foto producto", upload_to="productos")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    oferta = models.BooleanField(null=True, blank=True)
    precio_oferta = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    # A traves de la talla se sabe si hay o no disponibilidad del producto
    talla = models.ManyToManyField(Talla, through="Producto_Talla")
    producto_color = models.ManyToManyField(Color)
    producto_marca = models.ManyToManyField(Marca)
    producto_ajuste = models.ManyToManyField(Ajuste)
    producto_tipo_prenda = models.ManyToManyField(Tipo_Prenda)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")

    # @property
    # def hay_stock(self):
    #     pass

    def __str__(self):
        return self.nombre + ", " + self.referencia


    # EDITAR ESTO
    # def save(self, *args, **kwargs):
    #     print('pene')
    #     self.full_clean()  # Validate the model instance
    #     super().save(*args, **kwargs)
    #     self.refresh_from_db()
    #     tipo_prendas = self.producto_tipo_prenda.all()
    #     for tipo_prenda in tipo_prendas:
    #         print(tipo_prenda)

    # def clean(self):
    #     super().clean()
    #     if self.categoria and self.producto_tipo_prenda:
    #         if self.producto_tipo_prenda.categoria_padre != self.categoria:
    #             raise ValidationError(
    #                 {
    #                     "producto_tipo_prenda": "El tipo de prenda no es válido para la categoría seleccionada"
    #                 }
    #             )

    def clean(self):
        if not self.categoria:
            raise ValidationError({"categoria": "La categoría es obligatoria."})


class Producto_Talla(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    talla = models.ForeignKey(Talla, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.tala + "(" + self.cantidad + ")"

    class Meta:
        verbose_name = "Talla del Producto"
        verbose_name_plural = "Talla del Producto"
