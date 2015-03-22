# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0003_auto_20150320_1810'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alumnos',
            options={'verbose_name': 'Alumno', 'verbose_name_plural': 'Alumnos'},
        ),
    ]
