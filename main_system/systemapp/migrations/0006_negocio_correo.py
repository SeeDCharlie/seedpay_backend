# Generated by Django 3.2.6 on 2021-09-16 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemapp', '0005_auto_20210915_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='negocio',
            name='correo',
            field=models.EmailField(default=None, max_length=250),
            preserve_default=False,
        ),
    ]