# Generated by Django 2.2.6 on 2020-01-09 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0006_auto_20191208_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
