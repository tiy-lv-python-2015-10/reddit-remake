# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reddits', '0004_auto_20151024_2338'),
    ]

    operations = [
        migrations.CreateModel(
            name='VotingSystem',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('upvote', models.NullBooleanField()),
                ('downvote', models.NullBooleanField()),
                ('time_made', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(blank=True, null=True, to='reddits.Comment')),
                ('post', models.ForeignKey(blank=True, null=True, to='reddits.Post')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
