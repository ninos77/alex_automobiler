# Generated by Django 3.1.5 on 2021-02-11 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_remove_style_model_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='make',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.make'),
        ),
    ]
