# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-28 10:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('search', '0002_auto_20160924_1002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(max_length=255)),
                ('subscribed_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Topics')),
            ],
            options={
                'db_table': 'Subscribers',
                'verbose_name_plural': 'Subscribers',
            },
        ),
    ]