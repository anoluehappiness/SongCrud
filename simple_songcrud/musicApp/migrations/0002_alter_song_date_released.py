# Generated by Django 4.1.3 on 2022-11-04 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='date_released',
            field=models.DateField(),
        ),
    ]