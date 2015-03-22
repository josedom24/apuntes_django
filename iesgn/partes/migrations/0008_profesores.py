# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0007_remove_cursos_abr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre', models.CharField(max_length=20)),
                ('Apellidos', models.CharField(max_length=30)),
                ('Telefono', models.CharField(max_length=9, blank=True)),
                ('Movil', models.CharField(max_length=9, blank=True)),
                ('Email', models.EmailField(max_length=75)),
                ('Departamento', models.CharField(max_length=11, blank=True)),
                ('Baja', models.BooleanField(default=False)),
                ('Ce', models.BooleanField(default=False, verbose_name=b'Consejo Escolar')),
                ('Etcp', models.BooleanField(default=False)),
                ('Tic', models.BooleanField(default=False)),
                ('Bil', models.BooleanField(default=False, verbose_name=b'Biling\xc3\xbce')),
                ('Tutor', models.ForeignKey(to='partes.Cursos')),
            ],
            options={
                'verbose_name': 'Profesor',
                'verbose_name_plural': 'Profesores',
            },
            bases=(models.Model,),
        ),
    ]
