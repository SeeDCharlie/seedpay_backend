# Generated by Django 3.2.6 on 2021-09-17 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemapp', '0006_negocio_correo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='negocio',
            name='nit',
        ),
        migrations.AlterField(
            model_name='negocio',
            name='nombre',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=70),
        ),
    ]
