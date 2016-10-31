# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-25 17:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30, null=True)),
                ('phoneNumber', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('time', models.DateField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]