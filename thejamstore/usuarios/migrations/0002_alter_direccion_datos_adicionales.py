# Generated by Django 4.2.1 on 2023-05-21 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion',
            name='datos_adicionales',
            field=models.TextField(blank=True, null=True),
        ),
    ]
