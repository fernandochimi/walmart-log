# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wal_log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(primary_key=True, default=uuid.uuid4, serialize=False, max_length=128, unique=True, verbose_name='token'),
        ),
    ]
