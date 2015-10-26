# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subreddit', '0006_commentupvote_postupvote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trophies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, default='empty')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('trophy', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
