# Generated by Django 3.0.5 on 2021-01-13 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0017_participant_responsible'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='responsible',
            new_name='is_responsible',
        ),
    ]