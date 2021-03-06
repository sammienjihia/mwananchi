# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-24 10:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='keywords',
            options={'verbose_name_plural': 'Keywords'},
        ),
        migrations.AlterModelOptions(
            name='topics',
            options={'verbose_name_plural': 'Topics'},
        ),
        migrations.RemoveField(
            model_name='keywords',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='topics',
            name='publisher',
        ),
        migrations.AddField(
            model_name='topics',
            name='publication_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 9, 24, 10, 2, 16, 835020, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='keywords',
            name='publication_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
