# Generated by Django 4.2.4 on 2023-09-09 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsistema', '0002_compras_equipos_personal_trabajos_delete_juegos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipos',
            name='producto',
        ),
        migrations.AddField(
            model_name='equipos',
            name='estado',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personal',
            name='fecha_ingreso',
            field=models.DateField(),
        ),
    ]
