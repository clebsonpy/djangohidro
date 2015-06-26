# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hidrosite', '0002_auto_20150626_0657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serie_Temporal',
            fields=[
                ('Serie_Temporal_ID', models.IntegerField(primary_key=True)),
                ('Data_Hora', models.DateTimeField(serialize=False, primary_key=True)),
                ('Dado', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('Unidade_ID', models.AutoField(serialize=False, primary_key=True)),
                ('Tipo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Variavel',
            fields=[
                ('Variavel_ID', models.AutoField(serialize=False, primary_key=True)),
                ('Variavel', models.CharField(max_length=20)),
            ],
        ),
    ]
