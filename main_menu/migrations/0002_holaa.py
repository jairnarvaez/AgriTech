# Generated by Django 4.2.5 on 2023-11-19 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='holaa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_date', models.CharField(max_length=30)),
                ('data_value', models.IntegerField()),
            ],
        ),
    ]
