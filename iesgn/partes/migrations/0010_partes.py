# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0009_auto_20150322_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Tipo', models.CharField(default=b'a', max_length=1, choices=[(b'a', b'Amonestaci\xc3\xb3n'), (b'c', b'Citaci\xc3\xb3n'), (b's', b'Sanci\xc3\xb3n')])),
                ('Fecha', models.DateField(auto_now=True)),
                ('Fecha_fin', models.DateField()),
                ('Hora', models.CharField(default=b'1', max_length=1, choices=[(b'1', b'Primera'), (b'2', b'Segunda'), (b'3', b'Tercera'), (b'4', b'Recreo'), (b'5', b'Cuarta'), (b'6', b'Quinta'), (b'7', b'Sexta')])),
                ('Sancion', models.CharField(max_length=100, blank=True)),
                ('Comentario', models.TextField(blank=True)),
                ('Ida', models.ForeignKey(to='partes.Alumnos')),
                ('Profesor', models.ForeignKey(to='partes.Profesores')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
