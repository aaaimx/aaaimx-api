# Generated by Django 2.2.6 on 2019-11-21 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productivity', '0002_auto_20191121_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research',
            name='title',
            field=models.TextField(default=''),
        ),
    ]
