# Generated by Django 3.1.6 on 2021-02-27 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0021_auto_20210208_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='logistic.event'),
        ),
    ]
