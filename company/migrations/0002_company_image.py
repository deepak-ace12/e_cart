# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-30 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='company_logo'),
        ),
    ]
