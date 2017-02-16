# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-24 09:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyWords',
            fields=[
                ('key_word_id', models.AutoField(primary_key=True, serialize=False)),
                ('key_word', models.CharField(max_length=100)),
                ('publication_date', models.DateTimeField()),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Keywords',
            },
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('topic_id', models.AutoField(primary_key=True, serialize=False)),
                ('topic_title', models.CharField(max_length=255)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Topics',
            },
        ),
        migrations.AddField(
            model_name='keywords',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twittersearch.Topics'),
        ),
    ]