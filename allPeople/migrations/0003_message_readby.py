# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-09 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allPeople', '0002_followers_following'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='readBy',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
