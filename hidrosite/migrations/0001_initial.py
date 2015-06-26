# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discretizacao',
            fields=[
                ('Discretizacao_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Tipo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Fonte',
            fields=[
                ('Fonte_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Tipo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel_de_Consistencia',
            fields=[
                ('Tipo_Dados_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Nivel', models.CharField(max_length=20)),
            ],
        ),
    ]
