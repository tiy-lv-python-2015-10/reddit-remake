# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subreddit', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voting',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('up_or_down', models.BooleanField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('comment_upvotes', models.ForeignKey(to='subreddit.Comment')),
                ('post_upvotes', models.ForeignKey(to='subreddit.Post')),
            ],
        ),
    ]
