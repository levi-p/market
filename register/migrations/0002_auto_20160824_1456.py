# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-24 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign_up',
            name='Email',
            field=models.EmailField(blank=True, default='h', max_length=254),
        ),
        migrations.AlterField(
            model_name='sign_up',
            name='Name',
            field=models.CharField(default='h', max_length=30),
        ),
        migrations.AlterField(
            model_name='sign_up',
            name='enter_password',
            field=models.CharField(default='h', max_length=30),
        ),
        migrations.AlterField(
            model_name='sign_up',
            name='password',
            field=models.CharField(default='h', max_length=30),
        ),
    ]
