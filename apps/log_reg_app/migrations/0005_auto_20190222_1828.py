# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-22 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_reg_app', '0004_remove_quote_user_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
