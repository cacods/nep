# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-15 17:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0006_group_experiment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='experiment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiments.Experiment'),
        ),
    ]