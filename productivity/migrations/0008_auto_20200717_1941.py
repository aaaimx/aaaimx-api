# Generated by Django 3.0.5 on 2020-07-17 19:41

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productivity', '0007_auto_20200717_0546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='divisions',
        ),
        migrations.AddField(
            model_name='member',
            name='divisions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), blank=True, default=list, null=True, size=10),
        ),
        migrations.RemoveField(
            model_name='research',
            name='lines',
        ),
        migrations.AddField(
            model_name='research',
            name='lines',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), blank=True, default=list, null=True, size=20),
        ),
    ]