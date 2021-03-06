# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 16:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0003_auto_20160412_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='date_published',
            field=models.DateField(auto_now=True, default=datetime.datetime(2016, 4, 13, 16, 2, 42, 687968, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='cover_photo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cover', to='imager_images.Album'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='date_modified',
            field=models.DateField(auto_now=True),
        ),
    ]
