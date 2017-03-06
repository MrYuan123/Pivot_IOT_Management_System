# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 14:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0003_auto_20161220_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='SN',
            field=models.CharField(max_length=10, unique='true'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='name',
            field=models.CharField(max_length=10, unique='true'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='state',
            field=models.CharField(max_length=10, unique='false'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='temperature',
            field=models.CharField(max_length=10, unique='false'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='time',
            field=models.CharField(max_length=10, unique='false'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='machine',
            name='warning',
            field=models.CharField(max_length=10, unique='false'),
        ),
    ]