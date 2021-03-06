# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-22 18:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log_reg_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=55)),
                ('quote', models.TextField()),
                ('likes', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to='log_reg_app.User')),
            ],
        ),
    ]
