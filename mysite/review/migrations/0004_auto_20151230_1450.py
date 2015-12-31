# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_auto_20151230_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='synopsis',
            field=models.TextField(max_length=20),
        ),
    ]
