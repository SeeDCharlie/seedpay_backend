# Generated by Django 3.2.6 on 2021-09-17 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemapp', '0007_auto_20210917_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='negocio',
            name='direccion',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='negocio',
            name='telefono',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='negocio',
            name='telefono1',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='negocio',
            name='telefono2',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
    ]