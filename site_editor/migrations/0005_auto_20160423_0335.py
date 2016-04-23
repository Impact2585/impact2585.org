# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_editor', '0004_auto_20160419_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Robots',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('robot_name', models.CharField(max_length=100)),
                ('game_name', models.CharField(max_length=100)),
                ('game_year', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('robot_image', models.ImageField(upload_to=b'public/static/media/photos/')),
                ('competition', models.CharField(max_length=1, choices=[(b'0', b'FRC'), (b'1', b'VEX')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sponsors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sponsor_image', models.ImageField(upload_to=b'public/static/media/sponsors')),
                ('sponsor_tier', models.CharField(max_length=1, choices=[(b'0', b'Platinum'), (b'1', b'Gold'), (b'2', b'Bronze')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='robots',
            unique_together=set([('robot_name', 'game_name', 'description', 'competition')]),
        ),
    ]
