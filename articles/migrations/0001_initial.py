# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-16 06:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import markdownx.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', markdownx.models.MarkdownxField()),
                ('published_date', models.DateTimeField(default=datetime.datetime.now)),
                ('keywords', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]