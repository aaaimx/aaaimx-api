# Generated by Django 2.2.6 on 2019-11-17 06:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0002_auto_20191117_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='exp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 18, 6, 21, 36, 148605)),
        ),
    ]