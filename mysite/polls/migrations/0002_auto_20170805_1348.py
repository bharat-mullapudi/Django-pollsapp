# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-05 13:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Chioce',
            new_name='Choice',
        ),
    ]
