# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-10 02:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20170809_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='mobile_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
