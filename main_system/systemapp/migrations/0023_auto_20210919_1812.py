# Generated by Django 3.2.6 on 2021-09-19 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemapp', '0022_alter_negocio_calificacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='calificacion',
            field=models.DecimalField(blank=True, decimal_places=1, default=5, max_digits=2, null=True),
        ),
        migrations.AddField(
            model_name='servicio',
            name='calificacion',
            field=models.DecimalField(blank=True, decimal_places=1, default=5, max_digits=2, null=True),
        ),
    ]
