# Generated by Django 3.2.6 on 2021-10-25 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemapp', '0032_alter_factura_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='estado',
            field=models.CharField(choices=[('AT', 'Atendido'), ('PE', 'Pendiente'), ('RE', 'Rechazado'), ('CA', 'Cancelado')], default='PE', max_length=2, null=True),
        ),
    ]
