# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-02 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0020_auto_20161128_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='article_details',
            name='public',
            field=models.CharField(choices=[('1', 'yes'), ('2', 'no')], default=1, max_length=5, null=True),
        ),
    ]