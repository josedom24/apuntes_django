# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0004_auto_20150321_1923'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cursos',
            options={'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
    ]
