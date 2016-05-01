# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 17:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import datetime
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='img_name',
        ),
        migrations.AddField(
            model_name='photo',
            name='cover_photo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cover', to='imager_images.Album'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='date_created',
            field=models.DateField(auto_now_add=True, default=datetime.datetime.now()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='date_modified',
            field=models.DateField(default=datetime.datetime.now()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='desc',
            field=models.TextField(default=datetime.datetime.now()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='published',
            field=models.CharField(choices=[('pr', 'Private'), ('s', 'Shared'), ('pub', 'Public')], default='pub', max_length=30),
        ),
        migrations.AddField(
            model_name='photo',
            name='title',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='album',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]