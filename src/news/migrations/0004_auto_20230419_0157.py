# Generated by Django 2.2.1 on 2023-04-19 01:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20230418_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 19, 1, 57, 47, 224608)),
        ),
    ]
