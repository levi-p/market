# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-22 16:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20160822_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article_details',
            name='Id',
        ),
        migrations.AlterField(
            model_name='article_details',
            name='time',
            field=models.DateField(default=datetime.datetime(2016, 8, 22, 16, 27, 11, 216822)),
        ),
    ]
