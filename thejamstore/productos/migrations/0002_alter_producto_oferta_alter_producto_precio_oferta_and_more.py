# Generated by Django 4.2.1 on 2023-05-16 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='oferta',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio_oferta',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='producto_tipo_prenda',
            field=models.ForeignKey(blank=True, limit_choices_to=models.Q(('categoria_padre_id__isnull', False)), null=True, on_delete=django.db.models.deletion.SET_NULL, to='productos.tipo_prenda'),
        ),
    ]