# Generated by Django 4.2.1 on 2023-06-14 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_alter_custom_user_foto_perfil'),
        ('pedidos', '0010_alter_pedido_options_alter_pedido_producto_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='direccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usuarios.direccion'),
        ),
    ]
