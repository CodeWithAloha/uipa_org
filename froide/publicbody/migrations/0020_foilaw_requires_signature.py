# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-09 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicbody', '0019_foilaw_law_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='foilaw',
            name='requires_signature',
            field=models.BooleanField(default=False, verbose_name='Requires signature'),
        ),
    ]
