# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-19 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_blog_it', '0012_post_meta_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
