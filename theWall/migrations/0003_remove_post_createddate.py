# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theWall', '0002_auto_20171121_2305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='createdDate',
        ),
    ]
