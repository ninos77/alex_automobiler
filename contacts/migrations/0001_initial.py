# Generated by Django 3.1.5 on 2021-02-12 23:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='fulde navn')),
                ('email', models.EmailField(max_length=255)),
                ('car_id', models.IntegerField()),
                ('car_title', models.CharField(max_length=255, verbose_name='Biltitel')),
                ('customer_need', models.CharField(max_length=255, verbose_name='kundebehov')),
                ('message', models.CharField(blank=True, max_length=255, verbose_name='kommentar')),
                ('user_id', models.IntegerField()),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
