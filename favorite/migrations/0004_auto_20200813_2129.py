# Generated by Django 3.1 on 2020-08-13 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorite', '0003_auto_20200813_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockinfo',
            name='create_date',
            field=models.DateTimeField(),
        ),
    ]