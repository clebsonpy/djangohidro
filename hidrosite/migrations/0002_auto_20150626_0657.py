# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hidrosite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posto',
            fields=[
                ('Posto_ID', models.AutoField(serialize=False, primary_key=True)),
                ('Codigo_ANA', models.CharField(null=True, max_length=15)),
                ('Fonte_ID', models.ForeignKey(to='hidrosite.Fonte')),
            ],
        ),
        migrations.CreateModel(
            name='Reducao',
            fields=[
                ('Reducao_ID', models.AutoField(serialize=False, primary_key=True)),
                ('Tipo', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Posto',
            fields=[
                ('Tipo_Posto_ID', models.AutoField(serialize=False, primary_key=True)),
                ('Tipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='posto',
            name='Tipo_Posto_ID',
            field=models.ForeignKey(to='hidrosite.Tipo_Posto'),
        ),
    ]
