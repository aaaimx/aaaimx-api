# Generated by Django 3.1.6 on 2021-02-19 07:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('productivity', '0009_auto_20210104_0114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advisor',
            name='member',
        ),
        migrations.RemoveField(
            model_name='advisor',
            name='research',
        ),
        migrations.RemoveField(
            model_name='author',
            name='member',
        ),
        migrations.RemoveField(
            model_name='author',
            name='research',
        ),
        migrations.DeleteModel(
            name='Line',
        ),
        migrations.RemoveField(
            model_name='project',
            name='collaborators',
        ),
        migrations.RemoveField(
            model_name='project',
            name='institute',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.RenameField(
            model_name='research',
            old_name='resume',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='research',
            old_name='lines',
            new_name='tags',
        ),
        migrations.RemoveField(
            model_name='research',
            name='event',
        ),
        migrations.RemoveField(
            model_name='research',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='research',
            name='link',
        ),
        migrations.RemoveField(
            model_name='research',
            name='projects',
        ),
        migrations.RemoveField(
            model_name='research',
            name='pub_in',
        ),
        migrations.RemoveField(
            model_name='research',
            name='pub_type',
        ),
        migrations.RemoveField(
            model_name='research',
            name='year',
        ),
        migrations.AddField(
            model_name='member',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='research',
            name='banner',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='research',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='research',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='research',
            name='type',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.DeleteModel(
            name='Advisor',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
