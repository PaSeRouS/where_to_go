# Generated by Django 3.1.2 on 2022-08-25 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0015_auto_20220822_1545'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['position']},
        ),
        migrations.RenameField(
            model_name='image',
            old_name='position_id',
            new_name='position',
        ),
    ]
