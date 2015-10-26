# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reddits', '0003_auto_20151024_2306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='creation_time',
            new_name='created_time',
        ),
    ]
