# Generated by Django 3.1.2 on 2022-08-22 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_auto_20220820_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(max_length=300, verbose_name='Короткое описание'),
        ),
    ]
