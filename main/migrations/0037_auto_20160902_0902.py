# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 09:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_auto_20160831_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='time',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='product',
            name='category_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Category'),
        ),
    ]
