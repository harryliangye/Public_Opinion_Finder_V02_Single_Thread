# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Search_Engine', '0003_auto_20151012_0110'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Current_Linkpool',
        ),
    ]
