# Generated by Django 4.2.1 on 2023-05-23 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_alter_producto_talla_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='talla',
            options={'ordering': ('talla',)},
        ),
        migrations.AlterField(
            model_name='ajuste',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación'),
        ),
        migrations.AlterField(
            model_name='ajuste',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(choices=[('Superior', 'Superior'), ('Inferior', 'Inferior'), ('Accesorios', 'Accesorios'), ('Zapatillas', 'Zapatillas')], max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación'),
        ),
        migrations.AlterField(
            model_name='color',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación'),
        ),
        migrations.AlterField(
            model_name='color',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación'),
        ),
        migrations.AlterField(
            model_name='marca',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación'),
        ),
        migrations.AlterField(
            model_name='marca',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='productos.categoria', verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación'),
        ),
        migrations.AlterField(
            model_name='talla',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación'),
        ),
        migrations.AlterField(
            model_name='talla',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación'),
        ),
        migrations.AlterField(
            model_name='tipo_prenda',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación'),
        ),
        migrations.AlterField(
            model_name='tipo_prenda',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación'),
        ),
    ]
