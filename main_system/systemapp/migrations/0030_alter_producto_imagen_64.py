# Generated by Django 3.2.6 on 2021-10-22 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemapp', '0029_auto_20211021_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen_64',
            field=models.CharField(default='https://seedpaybuck.s3.sa-east-1.amazonaws.com/usuarios/71276688-7770-4a41-a7a2-24bd867043a1.jpg', max_length=256, null=True),
        ),
    ]