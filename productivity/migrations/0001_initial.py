# Generated by Django 2.2.6 on 2019-10-06 02:53

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('alias', models.CharField(max_length=100, unique=True)),
                ('logo', models.ImageField(default=None, null=True, upload_to='logos')),
                ('type', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('date_joined', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('division', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=False)),
                ('roles', django_mysql.models.ListTextField(models.CharField(max_length=50), size=10)),
                ('charge', models.CharField(max_length=100)),
                ('lastname', models.TextField(blank=True, default='')),
                ('adscription', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='productivity.Partner')),
            ],
        ),
    ]