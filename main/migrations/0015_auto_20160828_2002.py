# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 20:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20160828_2001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='category_name',
        ),
        migrations.AlterField(
            model_name='product',
            name='category_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Category'),
        ),
    ]
