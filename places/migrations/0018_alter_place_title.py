# Generated by Django 4.1 on 2022-09-01 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0017_alter_image_id_alter_place_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place",
            name="title",
            field=models.CharField(
                max_length=100, unique=True, verbose_name="Название места"
            ),
        ),
    ]
