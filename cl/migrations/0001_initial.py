# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-04 12:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0009_auto_20170908_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContingentLeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
                ('wascllastyear', models.CharField(max_length=3)),
                ('iscrcurrently', models.CharField(max_length=3)),
                ('hasporcurrently', models.CharField(max_length=3)),
                ('timesmiattended', models.IntegerField()),
                ('nocpiclink', models.TextField()),
                ('clprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile')),
            ],
        ),
    ]
