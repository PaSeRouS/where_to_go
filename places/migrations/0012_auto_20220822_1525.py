# Generated by Django 3.1.2 on 2022-08-22 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_auto_20220822_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(verbose_name='Короткое описание'),
        ),
    ]