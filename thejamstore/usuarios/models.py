from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Add your custom fields here
    telefono = models.CharField(max_length=20)
    # direccion = models.ForeignKey(ON DELETE SET NULL)
    # categoria = models.ForeignKey(ON DELETE SET NULL)