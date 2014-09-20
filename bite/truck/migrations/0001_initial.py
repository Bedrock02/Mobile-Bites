# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(null=True, unique=True, max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('Location', models.ForeignKey(to='location.Location', null=True)),
            ],
            options={
                'db_table': 'truck',
            },
            bases=(models.Model,),
        ),
    ]
