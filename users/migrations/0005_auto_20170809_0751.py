# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-09 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170808_0154'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='dob',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='fb_id',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
