# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0008_profesores'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Abr', models.CharField(max_length=4)),
                ('Nombre', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='profesores',
            name='Departamento',
            field=models.ForeignKey(to='partes.Departamentos'),
            preserve_default=True,
        ),
    ]
