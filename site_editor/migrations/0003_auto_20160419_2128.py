# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_editor', '0002_auto_20160419_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='carousel_image',
            field=models.ImageField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='media',
            name='image',
            field=models.ImageField(upload_to=b''),
        ),
    ]
