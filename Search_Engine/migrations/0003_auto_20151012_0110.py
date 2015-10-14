# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Search_Engine', '0002_current_linkpool_entry_linkpool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='current_linkpool',
            name='link',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='entry_linkpool',
            name='link',
            field=models.CharField(max_length=2000),
        ),
    ]
