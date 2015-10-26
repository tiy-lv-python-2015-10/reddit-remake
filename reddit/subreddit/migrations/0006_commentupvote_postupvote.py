# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subreddit', '0005_auto_20151025_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentUpvote',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('up_or_down', models.BooleanField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('comment_upvotes', models.ForeignKey(to='subreddit.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='PostUpvote',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('up_or_down', models.BooleanField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('post_upvotes', models.ForeignKey(to='subreddit.Post')),
            ],
        ),
    ]
