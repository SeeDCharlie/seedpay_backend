# Generated by Django 3.2.6 on 2021-09-18 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemapp', '0014_auto_20210918_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categorias',
            field=models.ManyToManyField(to='systemapp.categoria_productos'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='categorias',
            field=models.ManyToManyField(to='systemapp.categoria_servicios'),
        ),
    ]