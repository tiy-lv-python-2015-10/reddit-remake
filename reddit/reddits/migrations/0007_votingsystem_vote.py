# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reddits', '0006_auto_20151025_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='votingsystem',
            name='vote',
            field=models.NullBooleanField(),
        ),
    ]
