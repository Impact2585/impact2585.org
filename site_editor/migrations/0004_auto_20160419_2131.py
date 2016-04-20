# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_editor', '0003_auto_20160419_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='carousel_image',
            field=models.ImageField(upload_to=b'public/static/media/home/'),
        ),
        migrations.AlterField(
            model_name='media',
            name='image',
            field=models.ImageField(upload_to=b'public/static/media/photos/'),
        ),
    ]
