# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-10 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proshows', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proshowsevent',
            name='subtitle',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proshowsgenre',
            name='image',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]