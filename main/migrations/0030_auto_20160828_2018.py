# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 20:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20160828_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Category'),
        ),
    ]
