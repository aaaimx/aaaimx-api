# Generated by Django 3.1.6 on 2021-02-19 08:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('productivity', '0010_auto_20210219_0128'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Partner',
        ),
        migrations.DeleteModel(
            name='Research',
        ),
        migrations.RemoveField(
            model_name='division',
            name='story',
        ),
        migrations.AddField(
            model_name='division',
            name='color',
            field=models.CharField(default='', max_length=8),
        ),
        migrations.AddField(
            model_name='division',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='division',
            name='fanpage',
            field=models.URLField(default='', max_length=6),
        ),
        migrations.AddField(
            model_name='division',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='division',
            name='logo',
            field=models.URLField(default=''),
        ),
    ]
