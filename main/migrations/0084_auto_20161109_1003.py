# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-09 10:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0083_auto_20161103_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='category_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Category'),
        ),
    ]