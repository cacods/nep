# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0004_experiment_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='data_acquisition_done',
            field=models.BooleanField(default=False),
        ),
    ]