# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 20:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20160828_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category_name',
        ),
    ]
