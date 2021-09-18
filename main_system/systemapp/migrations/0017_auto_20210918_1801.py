# Generated by Django 3.2.6 on 2021-09-18 23:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('systemapp', '0016_auto_20210918_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='domiciliario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='domiciliario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='factura',
            name='vendedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='vendedor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='factura',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='cliente', to=settings.AUTH_USER_MODEL),
        ),
    ]
