# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-01 07:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20170930_1327'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Invoice',
        ),
    ]
