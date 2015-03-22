# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre', models.CharField(max_length=50)),
                ('DNI', models.CharField(max_length=9)),
                ('Direccion', models.CharField(max_length=60)),
                ('CodPostal', models.CharField(max_length=5)),
                ('Localidad', models.CharField(max_length=30)),
                ('Fecha_nacimiento', models.DateField(verbose_name=b'Fecha de nacimiento')),
                ('Provincia', models.CharField(max_length=30)),
                ('Ap1tutor', models.CharField(max_length=20)),
                ('Ap2tutor', models.CharField(max_length=20)),
                ('Nomtutor', models.CharField(max_length=20)),
                ('Telefono1', models.CharField(max_length=12)),
                ('Telefono2', models.CharField(max_length=12)),
                ('Obs', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Abr', models.CharField(max_length=15)),
                ('Curso', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.AddField(
            model_name='alumnos',
            name='Unidad',
            field=models.ForeignKey(to='partes.Cursos'),
            preserve_default=True,
        ),
    ]
