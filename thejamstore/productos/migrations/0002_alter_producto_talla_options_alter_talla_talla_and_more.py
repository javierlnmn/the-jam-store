# Generated by Django 4.2.1 on 2023-05-21 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto_talla',
            options={'verbose_name': 'Tallas de Productos', 'verbose_name_plural': 'Tallas de Productos'},
        ),
        migrations.AlterField(
            model_name='talla',
            name='talla',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='tipo_prenda',
            name='categoria_padre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.categoria', verbose_name='Categoría padre'),
        ),
    ]