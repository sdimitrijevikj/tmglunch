# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=512)),
                ('stars', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=128)),
                ('small_price', models.IntegerField()),
                ('large_price', models.IntegerField()),
                ('votes', models.IntegerField()),
                ('day', models.ForeignKey(to='website.Day')),
            ],
        ),
        migrations.AddField(
            model_name='feedback',
            name='food_item',
            field=models.ForeignKey(to='website.FoodItem'),
        ),
    ]
