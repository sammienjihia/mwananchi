# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-02-11 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0020_auto_20170211_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insms',
            name='msg_number',
            field=models.IntegerField(max_length=255),
        ),
    ]