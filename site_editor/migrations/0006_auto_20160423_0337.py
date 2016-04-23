# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_editor', '0005_auto_20160423_0335'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Robots',
            new_name='Robot',
        ),
        migrations.RenameModel(
            old_name='Sponsors',
            new_name='Sponsor',
        ),
    ]
