# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-30 10:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0021_auto_20161025_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('From', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from1', to='register.userprofile')),
                ('To', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to1', to='register.userprofile')),
            ],
        ),
    ]