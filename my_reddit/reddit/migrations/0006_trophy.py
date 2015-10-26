# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('reddit', '0005_auto_20151024_2359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trophy',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ManyToManyField(to='users.Profile')),
            ],
        ),
    ]
