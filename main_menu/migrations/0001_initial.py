# Generated by Django 4.2.5 on 2023-11-17 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_date', models.CharField(max_length=30)),
                ('data_value', models.IntegerField()),
            ],
        ),
    ]
