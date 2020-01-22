# Generated by Django 2.2.6 on 2020-01-22 07:23

import datetime
from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0043_auto_20200110_0513'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankmovement',
            name='file',
            field=models.ImageField(blank=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='voucher'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='exp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 1, 23, 7, 23, 49, 437989)),
        ),
    ]