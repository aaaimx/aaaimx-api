# Generated by Django 2.2.6 on 2019-11-27 05:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0022_auto_20191125_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='exp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 28, 5, 34, 54, 975791)),
        ),
    ]