# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-10 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserPreference', '0002_auto_20161010_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preference',
            name='I_like',
            field=models.CharField(max_length=70, null=True),
        ),
    ]
