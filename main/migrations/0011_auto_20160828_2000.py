# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 20:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20160828_1959'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categor',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.Category'),
        ),
    ]
