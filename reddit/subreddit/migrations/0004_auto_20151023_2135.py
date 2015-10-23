# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subreddit', '0003_comment_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True),
        ),
        migrations.AlterField(
            model_name='subreddit',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True),
        ),
    ]
