# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-23 07:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_auto_20160823_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article_details',
            name='time',
            field=models.DateField(default=datetime.datetime(2016, 8, 23, 7, 54, 41, 924258)),
        ),
    ]
