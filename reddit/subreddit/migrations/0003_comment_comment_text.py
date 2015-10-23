# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subreddit', '0002_auto_20151023_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_text',
            field=models.CharField(max_length=255, default='empty'),
        ),
    ]
