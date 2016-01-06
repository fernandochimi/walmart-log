# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wal_log', '0002_auto_20151004_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='transport',
            name='slug',
            field=models.SlugField(default=None, unique=True, verbose_name='slug'),
            preserve_default=False,
        ),
    ]
