# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-22 04:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('beds', models.CharField(max_length=100)),
                ('baths', models.CharField(max_length=100)),
                ('sqft', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
    ]
