# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-20 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='available',
            field=models.BooleanField(default=False),
        ),
    ]
