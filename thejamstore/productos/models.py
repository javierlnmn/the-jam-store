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
    nombre = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")

    def __str__(self):
        return self.nombre


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
    categoria_padre = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, verbose_name="Categoría padre"
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Tipo de Prenda"
        verbose_name_plural = "Tipos de Prenda"


class Talla(models.Model):
    talla = models.CharField(max_length=20, unique=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")

    def __str__(self):
        return self.talla


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

    @property
    def hay_stock(self):
        print(self.talla)
        return

    def __str__(self):
        return self.nombre + ", " + self.referencia

    def clean(self):
        if not self.categoria:
            raise ValidationError({"categoria": "Este campo es obligatorio"})


class Producto_Talla(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    talla = models.ForeignKey(Talla, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return (
            self.producto.__str__()
            + ". Talla "
            + self.talla.talla
            + ", "
            + str(self.cantidad)
            + " uds."
        )

    def clean(self):
        if not self.producto_id or not self.talla_id:
            raise ValidationError('')

        talla_producto = Producto_Talla.objects.filter(producto=self.producto, talla=self.talla).first()
        if talla_producto:
            self.id = talla_producto.id  # Override existing object by assigning its ID
            self._state.adding = False
            

    class Meta:
        verbose_name = "Tallas de Productos"
        verbose_name_plural = "Tallas de Productos"
