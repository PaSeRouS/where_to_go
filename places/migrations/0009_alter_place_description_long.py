# Generated by Django 4.1 on 2022-08-19 18:12

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0008_alter_place_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place",
            name="description_long",
            field=tinymce.models.HTMLField(verbose_name="Подробное описание"),
        ),
    ]