# Generated by Django 2.2.6 on 2019-12-08 02:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productivity', '0013_auto_20191207_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='board',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='membership',
            name='exp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 12, 9, 2, 19, 9, 662068)),
        ),
    ]
