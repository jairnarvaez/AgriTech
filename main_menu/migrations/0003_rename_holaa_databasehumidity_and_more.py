# Generated by Django 4.2.5 on 2023-11-19 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_menu', '0002_holaa'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='holaa',
            new_name='DataBaseHumidity',
        ),
        migrations.RenameModel(
            old_name='DataBase',
            new_name='DataBaseTemperature',
        ),
    ]
