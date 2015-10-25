# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reddits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subreddit',
            name='description',
            field=models.TextField(),
        ),
    ]
