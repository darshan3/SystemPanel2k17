# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-07 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitionsevent',
            name='maxparticipants',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='competitionsevent',
            name='minparticipants',
            field=models.IntegerField(default=0),
        ),
    ]
