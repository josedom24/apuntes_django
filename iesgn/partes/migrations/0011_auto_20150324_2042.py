# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0010_partes'),
    ]

    operations = [
        migrations.CreateModel(
            name='AltaMasiva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Fichero', models.FileField(upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='partes',
            options={'verbose_name': 'Parte', 'verbose_name_plural': 'Partes'},
        ),
        migrations.AlterField(
            model_name='partes',
            name='Fecha',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
