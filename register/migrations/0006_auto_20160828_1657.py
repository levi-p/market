# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 16:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20160828_1155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='use_r',
            new_name='first_name',
        ),
    ]
