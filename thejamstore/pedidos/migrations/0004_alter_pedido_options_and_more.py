# Generated by Django 4.2.1 on 2023-05-21 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_alter_pedido_options_pedido_numero_pedido'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedido',
            options={'ordering': ['codigo_pedido']},
        ),
        migrations.RenameField(
            model_name='pedido',
            old_name='numero_pedido',
            new_name='codigo_pedido',
        ),
    ]
