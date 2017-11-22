# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('theWall', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='createdDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 11, 22, 5, 5, 23, 653418, tzinfo=utc)),
        ),
    ]
