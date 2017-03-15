# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 14:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0006_study'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='study',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='experiments.Study'),
        ),
    ]