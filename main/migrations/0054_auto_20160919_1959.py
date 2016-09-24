# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-19 19:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0053_auto_20160919_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='participants',
            field=models.TextField(default=0),
        ),
    ]