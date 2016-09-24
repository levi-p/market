# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0049_auto_20160918_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='read',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category_name',
            field=models.ForeignKey(blank=True, to='main.Category', null=True),
        ),
    ]
