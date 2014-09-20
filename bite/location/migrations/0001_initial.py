# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('longitude', models.CharField(null=True, max_length=255)),
                ('latitude', models.CharField(null=True, max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True, auto_now_add=True)),
            ],
            options={
                'db_table': 'location',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together=set([('longitude', 'latitude')]),
        ),
    ]
