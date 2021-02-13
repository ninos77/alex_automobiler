# Generated by Django 3.1.5 on 2021-02-11 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_auto_20210211_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='make',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='make', to='cars.make', verbose_name='bilmærke'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='model', to='cars.model', verbose_name='model'),
        ),
    ]