# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 19:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cages', '0003_auto_20160703_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='zoocage',
            name='cage_name',
            field=models.CharField(default=datetime.datetime(2016, 7, 3, 19, 8, 48, 397001, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zoocage',
            name='cage_type',
            field=models.CharField(default=datetime.datetime(2016, 7, 3, 19, 8, 54, 973057, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
