# Generated by Django 2.2.6 on 2019-12-08 21:58

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('productivity', '0021_auto_20191208_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='thumbnailFile',
            field=models.ImageField(default=None, null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='thumbnail'),
        ),
        migrations.AlterField(
            model_name='member',
            name='thumbnailUrl',
            field=models.CharField(blank=True, default='https://drive.google.com/uc?id=', max_length=100),
        ),
    ]
