# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0004_auto_20151024_2327'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentDownVote',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('comm_down_vote', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(to='reddit.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='CommentUpVote',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('comm_up_vote', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(to='reddit.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='PostDownVote',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('post_down_vote', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostUpVote',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('post_up_vote', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length='50'),
        ),
        migrations.AddField(
            model_name='postupvote',
            name='post',
            field=models.ForeignKey(to='reddit.Post'),
        ),
        migrations.AddField(
            model_name='postdownvote',
            name='post',
            field=models.ForeignKey(to='reddit.Post'),
        ),
    ]
