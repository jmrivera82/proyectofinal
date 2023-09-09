# Generated by Django 4.2.4 on 2023-09-09 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsistema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numfactura', models.IntegerField()),
                ('monto', models.IntegerField()),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoint', models.IntegerField()),
                ('producto', models.CharField(max_length=30)),
                ('tipo', models.CharField(max_length=15)),
                ('descripcion', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('fecha_ingreso', models.DateTimeField()),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trabajos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('plataforma', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='juegos',
        ),
        migrations.DeleteModel(
            name='maquinas',
        ),
    ]
