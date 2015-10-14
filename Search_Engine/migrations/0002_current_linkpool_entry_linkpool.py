# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Search_Engine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Current_Linkpool',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('link', models.URLField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Entry_Linkpool',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('link', models.URLField(max_length=2000)),
            ],
        ),
    ]
