# Generated by Django 3.0.5 on 2020-06-09 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0011_auto_20200316_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='place',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]