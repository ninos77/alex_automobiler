# Generated by Django 3.1.5 on 2021-02-13 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_auto_20210211_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='vehicle_number',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='nummerplade'),
        ),
    ]
