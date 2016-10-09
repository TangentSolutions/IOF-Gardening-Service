# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-09 09:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(null=True)),
                ('humidity', models.FloatField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Data Reading',
                'verbose_name_plural': 'Data Readings',
            },
        ),
        migrations.CreateModel(
            name='Garden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Data Reading',
            },
        ),
        migrations.AddField(
            model_name='data',
            name='garden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Garden'),
        ),
    ]
