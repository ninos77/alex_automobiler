# Generated by Django 3.1.5 on 2021-02-23 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_car_vehicle_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10, verbose_name='pris'),
        ),
    ]
