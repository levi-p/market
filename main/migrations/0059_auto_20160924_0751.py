# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-24 07:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0058_auto_20160924_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
