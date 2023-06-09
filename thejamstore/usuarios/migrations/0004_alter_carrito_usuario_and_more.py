# Generated by Django 4.2.1 on 2023-05-22 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_custom_user_email_alter_custom_user_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario del carrito'),
        ),
        migrations.AlterField(
            model_name='categoria_usuario',
            name='categoria',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='custom_user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
