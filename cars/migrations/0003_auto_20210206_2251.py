# Generated by Django 3.1.5 on 2021-02-06 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20210206_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='is_featured',
            field=models.BooleanField(default=False, verbose_name='er vist'),
        ),
        migrations.AlterField(
            model_name='car',
            name='is_sold',
            field=models.BooleanField(default=False, verbose_name='sælges'),
        ),
    ]
