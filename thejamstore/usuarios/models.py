from django.contrib.auth.models import AbstractUser
from django.db import models

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


class Direccion(models.Model):
    pais = models.CharField(max_length=255, default="España")
    provincia = models.CharField(max_length=255, choices=PROVINCIAS_CHOICES)
    municipio = models.CharField(max_length=255)
    cod_postal = models.CharField(max_length=10)
    calle = models.CharField(max_length=255)
    numero = models.CharField(max_length=20)
    piso = models.CharField(max_length=20, null=True)
    puerta = models.CharField(max_length=20, null=True)
    datos_adicionales = models.TextField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")


class CategoriaUsuario(models.Model):
    categoria = models.CharField(
        max_length=255,
    )  # USUARIO / EMPRESA (son las opciones)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")


class CustomUser(AbstractUser):
    telefono = models.CharField(max_length=20)
    direccion = models.ForeignKey(Direccion, on_delete=models.SET_NULL)
    categoria = models.ForeignKey(CategoriaUsuario, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")
