# Generated by Django 4.2.1 on 2023-05-16 05:31

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Custom_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('telefono', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha de modificacion')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha de modificacion')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria_Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha de modificacion')),
            ],
        ),
        migrations.CreateModel(
            name='ListaDeseos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha de modificacion')),
                ('producto', models.ManyToManyField(to='productos.producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provincia', models.CharField(choices=[('AC', 'A Coruña'), ('AL', 'Álava'), ('AB', 'Albacete'), ('A', 'Alicante'), ('ALM', 'Almería'), ('O', 'Asturias'), ('AV', 'Ávila'), ('BA', 'Badajoz'), ('B', 'Barcelona'), ('BU', 'Burgos'), ('CC', 'Cáceres'), ('CA', 'Cádiz'), ('S', 'Cantabria'), ('CS', 'Castellón'), ('CR', 'Ciudad Real'), ('CO', 'Córdoba'), ('CU', 'Cuenca'), ('GI', 'Girona'), ('GR', 'Granada'), ('GU', 'Guadalajara'), ('SS', 'Guipúzcoa'), ('H', 'Huelva'), ('HU', 'Huesca'), ('PM', 'Illes Balears'), ('J', 'Jaén'), ('LO', 'La Rioja'), ('GC', 'Las Palmas'), ('LE', 'León'), ('L', 'Lleida'), ('LU', 'Lugo'), ('M', 'Madrid'), ('MA', 'Málaga'), ('MU', 'Murcia'), ('NA', 'Navarra'), ('OR', 'Ourense'), ('P', 'Palencia'), ('PO', 'Pontevedra'), ('SA', 'Salamanca'), ('TF', 'Santa Cruz de Tenerife'), ('SG', 'Segovia'), ('SE', 'Sevilla'), ('SO', 'Soria'), ('T', 'Tarragona'), ('TE', 'Teruel'), ('TO', 'Toledo'), ('V', 'Valencia'), ('VA', 'Valladolid'), ('BI', 'Vizcaya'), ('ZA', 'Zamora'), ('Z', 'Zaragoza')], max_length=255)),
                ('municipio', models.CharField(max_length=255)),
                ('cod_postal', models.CharField(max_length=10)),
                ('calle', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=20)),
                ('piso', models.CharField(max_length=20, null=True)),
                ('puerta', models.CharField(max_length=20, null=True)),
                ('datos_adicionales', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha de modificacion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(null=True)),
                ('valoracion', models.IntegerField(choices=[(1, 'Muy malo'), (2, 'Malo'), (3, 'Aceptable'), (4, 'Bueno'), (5, 'Excelente')])),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha de modificacion')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Carrito_Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.carrito')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
            ],
        ),
        migrations.AddField(
            model_name='carrito',
            name='producto',
            field=models.ManyToManyField(through='usuarios.Carrito_Productos', to='productos.producto'),
        ),
        migrations.AddField(
            model_name='carrito',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='custom_user',
            name='categoria',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.categoria_usuario'),
        ),
        migrations.AddField(
            model_name='custom_user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='custom_user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
