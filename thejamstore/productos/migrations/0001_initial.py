# Generated by Django 4.2.1 on 2023-05-21 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ajuste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha de modificacion')),
            ],
            options={
                'verbose_name': 'Ajuste de la Prenda',
                'verbose_name_plural': 'Ajuste de la Prenda',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('superior', 'Superior'), ('inferior', 'Inferior'), ('accesorios', 'Accesorios'), ('zapatillas', 'Zapatillas')], max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha de modificacion')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
                ('codigo_hex', models.CharField(max_length=7)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha de modificacion')),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colores',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha de modificacion')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('referencia', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='productos', verbose_name='foto producto')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('oferta', models.BooleanField(blank=True, null=True)),
                ('precio_oferta', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha de modificacion')),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='productos.categoria')),
                ('producto_ajuste', models.ManyToManyField(to='productos.ajuste')),
                ('producto_color', models.ManyToManyField(to='productos.color')),
                ('producto_marca', models.ManyToManyField(to='productos.marca')),
            ],
        ),
        migrations.CreateModel(
            name='Talla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talla', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha de modificacion')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Prenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha de modificacion')),
                ('categoria_padre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.categoria')),
            ],
            options={
                'verbose_name': 'Tipo de Prenda',
                'verbose_name_plural': 'Tipos de Prenda',
            },
        ),
        migrations.CreateModel(
            name='Producto_Talla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
                ('talla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.talla')),
            ],
            options={
                'verbose_name': 'Talla del Producto',
                'verbose_name_plural': 'Talla del Producto',
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='producto_tipo_prenda',
            field=models.ManyToManyField(to='productos.tipo_prenda'),
        ),
        migrations.AddField(
            model_name='producto',
            name='talla',
            field=models.ManyToManyField(through='productos.Producto_Talla', to='productos.talla'),
        ),
    ]
