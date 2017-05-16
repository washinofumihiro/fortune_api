# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 02:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ABTypeResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.TextField(verbose_name='占い結果')),
                ('date', models.CharField(default='', max_length=255, verbose_name='日付')),
            ],
        ),
        migrations.CreateModel(
            name='ATypeResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.TextField(verbose_name='占い結果')),
                ('date', models.CharField(default='', max_length=255, verbose_name='日付')),
            ],
        ),
        migrations.CreateModel(
            name='BloodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_type', models.CharField(default='', max_length=255, verbose_name='血液型')),
            ],
        ),
        migrations.CreateModel(
            name='BTypeResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.TextField(verbose_name='占い結果')),
                ('date', models.CharField(default='', max_length=255, verbose_name='日付')),
            ],
        ),
        migrations.CreateModel(
            name='OTypeResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.TextField(verbose_name='占い結果')),
                ('date', models.CharField(default='', max_length=255, verbose_name='日付')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.TextField(verbose_name='占い結果')),
                ('date', models.CharField(default='', max_length=255, verbose_name='日付')),
                ('blood_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='fortune_result.BloodType')),
            ],
        ),
    ]
