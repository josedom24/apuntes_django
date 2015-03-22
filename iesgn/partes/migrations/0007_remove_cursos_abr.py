# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0006_auto_20150321_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursos',
            name='Abr',
        ),
    ]
