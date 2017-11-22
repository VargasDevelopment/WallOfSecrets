# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('content', models.TextField()),
                ('key', models.CharField(max_length=140)),
                ('createdDate', models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 22, 3, 27, 55, 946365, tzinfo=utc))),
            ],
        ),
    ]
