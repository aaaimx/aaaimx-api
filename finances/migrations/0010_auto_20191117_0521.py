# Generated by Django 2.2.6 on 2019-11-17 05:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0009_auto_20191117_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='exp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 18, 5, 21, 9, 642827)),
        ),
    ]
