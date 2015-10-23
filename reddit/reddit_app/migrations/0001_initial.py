# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('modification_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subreddit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('creation_date_time', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='subreddit_rel',
            field=models.ForeignKey(to='reddit_app.Subreddit'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post_rel',
            field=models.ForeignKey(to='reddit_app.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_rel',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
