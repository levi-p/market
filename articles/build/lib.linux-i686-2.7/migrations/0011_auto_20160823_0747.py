# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-23 07:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20160822_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article_details',
            name='time',
            field=models.DateField(default=datetime.datetime(2016, 8, 23, 7, 47, 6, 309498)),
        ),
    ]
