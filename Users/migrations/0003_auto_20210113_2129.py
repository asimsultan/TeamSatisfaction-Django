# Generated by Django 2.2.11 on 2021-01-14 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20210113_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='happiness_date',
            field=models.DateField(unique=True),
        ),
    ]