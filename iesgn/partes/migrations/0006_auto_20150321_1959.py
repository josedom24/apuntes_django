# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0005_auto_20150321_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='Ap1tutor',
            field=models.CharField(max_length=20, verbose_name=b'Apellido 1 tutor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='Ap2tutor',
            field=models.CharField(max_length=20, verbose_name=b'Apellido 2 tutor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='CodPostal',
            field=models.CharField(max_length=5, verbose_name=b'C\xc3\xb3digo postal'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='Nomtutor',
            field=models.CharField(max_length=20, verbose_name=b'Nombre tutor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='Obs',
            field=models.TextField(verbose_name=b'Observaciones', blank=True),
            preserve_default=True,
        ),
    ]
