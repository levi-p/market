# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-09 15:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0068_auto_20161009_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='category_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Category'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
