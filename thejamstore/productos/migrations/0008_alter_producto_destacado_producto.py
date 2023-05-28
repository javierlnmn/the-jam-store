# Generated by Django 4.2.1 on 2023-05-28 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0007_remove_producto_destacado_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto_destacado',
            name='producto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='destacado', serialize=False, to='productos.producto', verbose_name='Producto destacado'),
        ),
    ]
