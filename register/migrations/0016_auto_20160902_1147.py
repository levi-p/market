# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0015_userprofile_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_id',
            field=models.IntegerField(blank=True),
        ),
    ]
