# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0002_auto_20150320_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='Obs',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='Telefono1',
            field=models.CharField(max_length=12, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='Telefono2',
            field=models.CharField(max_length=12, blank=True),
            preserve_default=True,
        ),
    ]
