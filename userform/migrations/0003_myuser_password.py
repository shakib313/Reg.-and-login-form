# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-23 00:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userform', '0002_myuser_your_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='password',
            field=models.IntegerField(default=123),
            preserve_default=False,
        ),
    ]