# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 00:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fortune_result', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='name',
            new_name='result',
        ),
    ]