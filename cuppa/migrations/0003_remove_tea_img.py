# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 16:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuppa', '0002_auto_20160527_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tea',
            name='img',
        ),
    ]
