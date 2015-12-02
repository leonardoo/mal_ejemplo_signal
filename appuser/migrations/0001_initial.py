# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalPlan',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, blank=True)),
            ],
            options={
                'verbose_name': 'HistorialPlan',
                'verbose_name_plural': 'HistorialPlans',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Plan',
                'verbose_name_plural': 'Plans',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('refercode', models.CharField(blank=True, max_length=100)),
                ('plan', models.ForeignKey(to='appuser.Plan')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.AddField(
            model_name='historicalplan',
            name='actual',
            field=models.ForeignKey(to='appuser.Plan'),
        ),
        migrations.AddField(
            model_name='historicalplan',
            name='owner',
            field=models.ForeignKey(to='appuser.User'),
        ),
    ]
