# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subreddit', '0004_voting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voting',
            name='comment_upvotes',
        ),
        migrations.RemoveField(
            model_name='voting',
            name='post_upvotes',
        ),
        migrations.DeleteModel(
            name='Voting',
        ),
    ]
