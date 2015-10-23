# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subreddit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=255, default='empty'),
        ),
        migrations.AddField(
            model_name='subreddit',
            name='description',
            field=models.CharField(max_length=255, default='empty'),
        ),
    ]
