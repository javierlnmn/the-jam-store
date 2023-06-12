from django.contrib.auth.models import AbstractUser
from django.db import models
from productos.models import Producto
from django.core.exceptions import ValidationError


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
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")

    def __str__(self):
        return (self.categoria).capitalize()

    class Meta:
        verbose_name = "Categoría de Usuario"
        verbose_name_plural = "Categorías de Usuario"


class Custom_User(AbstractUser):
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(blank=False, null=False)
    categoria = models.ForeignKey(
        Categoria_Usuario, on_delete=models.SET_NULL, null=True, blank=True, default="1"
    )
    foto_perfil = models.ImageField(null=True, blank=True, verbose_name="Avatar de usuario", upload_to="usuarios")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")

    def clean(self):
        if not self.categoria:
            raise ValidationError({"categoria": "Este campo es obligatorio"})
        
    def __str__(self):
        return self.username

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
    piso = models.CharField(max_length=20, null=True, blank=True)
    puerta = models.CharField(max_length=20, null=True, blank=True)
    datos_adicionales = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")
    
    @property
    def en_uso(self):
        from pedidos.models import Pedido
        for pedido in Pedido.objects.all():
            if pedido.direccion == self:
                return True
        return False

    def __str__(self):
        direccion_completa = (
            "("+self.usuario.username
            + ") " +
            self.provincia
            + ", "
            + self.municipio
            + ", "
            + self.cod_postal
            + ", "
            + self.calle
            + " "
            + self.numero
        )

        direccion_completa += " " + self.piso if self.piso else ""
        direccion_completa += " " + self.puerta if self.puerta else ""

        return direccion_completa

    class Meta:
        verbose_name = "Dirección"
        verbose_name_plural = "Direcciones"


class Carrito(models.Model):
    usuario = models.OneToOneField(
        Custom_User, on_delete=models.CASCADE, verbose_name="Usuario del carrito"
    )
    producto = models.ManyToManyField(Producto, through="Carrito_Productos")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")

    def __str__(self):
        return "Carrito de " + self.usuario.username


class Carrito_Productos(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    carrito = models.ForeignKey(
        Carrito,
        on_delete=models.CASCADE,
    )
    cantidad = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Producto del Carrito"
        verbose_name_plural = "Productos del Carrito"


class Lista_Deseos(models.Model):
    usuario = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")

    def __str__(self):
        return "Lista de deseos de " + self.usuario.username

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
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")

    def __str__(self):
        return "Comentario de " + self.usuario.username + " en " + str(self.producto)


class Peticiones(models.Model):
    nombre_producto = models.CharField(max_length=255)
    mensaje = models.TextField()
    imagen = models.ImageField()
    precio = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Precio solicitado",
    )
    talla = models.CharField(max_length=20)
    usuario = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")

    class Meta:
        verbose_name = "Petición"
        verbose_name_plural = "Peticiones"
