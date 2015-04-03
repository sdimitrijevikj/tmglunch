# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
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
                ('date', models.DateField()),
                ('name', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=128)),
                ('small_price', models.FloatField()),
                ('large_price', models.FloatField()),
                ('votes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MenuDocs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_from', models.DateField()),
                ('file', models.FileField(upload_to=b'menu')),
            ],
        ),
        migrations.AddField(
            model_name='feedback',
            name='food_item',
            field=models.ForeignKey(to='website.FoodItem'),
        ),
    ]
