# Generated by Django 3.2.6 on 2021-09-18 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemapp', '0017_auto_20210918_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categorias',
            field=models.ManyToManyField(blank=True, to='systemapp.categoria_productos'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='categorias',
            field=models.ManyToManyField(blank=True, to='systemapp.categoria_servicios'),
        ),
    ]