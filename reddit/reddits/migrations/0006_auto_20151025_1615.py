# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reddits', '0005_votingsystem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votingsystem',
            name='downvote',
        ),
        migrations.RemoveField(
            model_name='votingsystem',
            name='upvote',
        ),
    ]
