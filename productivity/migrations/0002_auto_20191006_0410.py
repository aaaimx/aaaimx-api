# Generated by Django 2.2.6 on 2019-10-06 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productivity', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='id',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='member',
            name='name',
        ),
        migrations.RemoveField(
            model_name='partner',
            name='id',
        ),
        migrations.AddField(
            model_name='member',
            name='fullname',
            field=models.CharField(default='', max_length=200, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AddField(
            model_name='partner',
            name='name',
            field=models.CharField(default='', max_length=200, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='adscription',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='productivity.Partner'),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='partner',
            name='alias',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='partner',
            name='type',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='role',
            name='id',
            field=models.CharField(default='', max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]