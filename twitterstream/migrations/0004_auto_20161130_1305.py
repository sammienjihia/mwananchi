# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-30 13:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitterstream', '0003_streamtweets_pub_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='streamtweets',
            old_name='pub_data',
            new_name='date',
        ),
    ]
