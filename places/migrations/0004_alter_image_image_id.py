# Generated by Django 3.2 on 2022-08-19 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_place_title_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_id',
            field=models.IntegerField(default=0, verbose_name='Номер по порядку'),
        ),
    ]