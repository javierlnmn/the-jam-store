from django.contrib.auth.models import AbstractUser
from django.db import models
from productos.models import Producto

PROVINCIAS_CHOICES = (
    ("AC", "A Coruña"),
    ("AL", "Álava"),
    ("AB", "Albacete"),
    ("A", "Alicante"),
    ("ALM", "Almería"),
    ("O", "Asturias"),
    ("AV", "Ávila"),
    ("BA", "Badajoz"),
    ("B", "Barcelona"),
    ("BU", "Burgos"),
    ("CC", "Cáceres"),
    ("CA", "Cádiz"),
    ("S", "Cantabria"),
    ("CS", "Castellón"),
    ("CR", "Ciudad Real"),
    ("CO", "Córdoba"),
    ("CU", "Cuenca"),
    ("GI", "Girona"),
    ("GR", "Granada"),
    ("GU", "Guadalajara"),
    ("SS", "Guipúzcoa"),
    ("H", "Huelva"),
    ("HU", "Huesca"),
    ("PM", "Illes Balears"),
    ("J", "Jaén"),
    ("LO", "La Rioja"),
    ("GC", "Las Palmas"),
    ("LE", "León"),
    ("L", "Lleida"),
    ("LU", "Lugo"),
    ("M", "Madrid"),
    ("MA", "Málaga"),
    ("MU", "Murcia"),
    ("NA", "Navarra"),
    ("OR", "Ourense"),
    ("P", "Palencia"),
    ("PO", "Pontevedra"),
    ("SA", "Salamanca"),
    ("TF", "Santa Cruz de Tenerife"),
    ("SG", "Segovia"),
    ("SE", "Sevilla"),
    ("SO", "Soria"),
    ("T", "Tarragona"),
    ("TE", "Teruel"),
    ("TO", "Toledo"),
    ("V", "Valencia"),
    ("VA", "Valladolid"),
    ("BI", "Vizcaya"),
    ("ZA", "Zamora"),
    ("Z", "Zaragoza"),
)


class Categoria_Usuario(models.Model):
    categoria = models.CharField(max_length=255)  # USUARIO / EMPRESA (son las opciones)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")
    
    def __str__(self):
        return self.categoria
    
    class Meta:
        verbose_name = "Categoría de Usuario"
        verbose_name_plural = "Categorías de Usuario"


class Custom_User(AbstractUser):
    telefono = models.CharField(max_length=20)
    categoria = models.ForeignKey(
        Categoria_Usuario, on_delete=models.SET_NULL, null=True, blank=True, default='1'
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")

    def save(self, *args, **kwargs):
        if not self.categoria:
            raise ValueError("La categoría es obligatoria.")
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


class Direccion(models.Model):
    # Damos por hecho que los pedidos se realizan únicamente en el territorio español por el momento
    # Si llegara a trriunfar, ampliaríamos nuestra oferta a otros países
    usuario = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    provincia = models.CharField(max_length=255, choices=PROVINCIAS_CHOICES)
    municipio = models.CharField(max_length=255)
    cod_postal = models.CharField(max_length=10)
    calle = models.CharField(max_length=255)
    numero = models.CharField(max_length=20)
    piso = models.CharField(max_length=20, null=True)
    puerta = models.CharField(max_length=20, null=True)
    datos_adicionales = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")


class Carrito(models.Model):
    usuario = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto, through="Carrito_Productos")
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")


class Carrito_Productos(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    
    class Meta:
        verbose_name = "Producto del Carrito"
        verbose_name_plural = "Productos del Carrito"


class Lista_Deseos(models.Model):
    usuario = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")
    
    class Meta:
        verbose_name = "Lista de Deseos"
        verbose_name_plural = "Listas de Deseos"


class Puntuacion_Valoracion(models.IntegerChoices):
    MUY_MALO = 1, "Muy malo"
    MALO = 2, "Malo"
    ACEPTABLE = 3, "Aceptable"
    BUENO = 4, "Bueno"
    EXCELENTE = 5, "Excelente"


class Comentario(models.Model):
    comentario = models.TextField(null=True)
    valoracion = models.IntegerField(choices=Puntuacion_Valoracion.choices)
    usuario = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")
    
class Peticiones(models.Model):
    nombre_producto = models.CharField(max_length=255)
    mensaje = models.TextField()
    imagen = models.ImageField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    talla = models.CharField(max_length=20)
    usuario = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")
