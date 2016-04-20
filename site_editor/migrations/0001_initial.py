# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='index',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('carousel_image', models.ImageField(upload_to=b'')),
                ('carousel_title', models.CharField(max_length=200)),
                ('carousel_description', models.CharField(max_length=750)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'')),
                ('year', models.IntegerField()),
                ('album', models.CharField(max_length=200)),
                ('competition', models.CharField(max_length=1, choices=[(b'0', b'FRC'), (b'1', b'VEX')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='media',
            unique_together=set([('album', 'competition')]),
        ),
        migrations.AlterUniqueTogether(
            name='index',
            unique_together=set([('carousel_title', 'carousel_description')]),
        ),
    ]
