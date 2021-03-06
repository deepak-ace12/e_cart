# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-01 10:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_delete_invoice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='company_name',
            new_name='company',
        ),
        migrations.RemoveField(
            model_name='item',
            name='company_name',
        ),
        migrations.AddField(
            model_name='item',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='project.Project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='products',
            field=models.ManyToManyField(related_name='item', to='project.Item'),
        ),
    ]
