# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-09 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0018_auto_20161009_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, default='youremail@email.com', max_length=254, null=True),
        ),
    ]
