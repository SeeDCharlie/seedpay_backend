# Generated by Django 3.2.6 on 2021-09-13 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0003_auto_20210912_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='celular',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True),
        ),
    ]