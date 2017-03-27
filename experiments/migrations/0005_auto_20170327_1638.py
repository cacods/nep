# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 16:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import experiments.models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0004_auto_20170327_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_birth', models.DateField(validators=[experiments.models.validate_date_birth])),
                ('district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('removed', models.BooleanField(default=False)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiments.Gender')),
                ('marital_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiments.MaritalStatus')),
            ],
        ),
        migrations.RenameField(
            model_name='group',
            old_name='experimental_protocol',
            new_name='protocol_component',
        ),
    ]
