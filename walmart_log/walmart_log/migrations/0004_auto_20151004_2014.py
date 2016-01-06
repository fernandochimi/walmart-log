# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('walmart_log', '0003_transport_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='map',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
