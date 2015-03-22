# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Cursos(models.Model):
	Abr = models.CharField(max_length=15)
	Curso = models.CharField(max_length=30)

	def __unicode__(self):
		return self.Abr+" - "+self.Curso

	class Meta:
		verbose_name="Curso"
		verbose_name_plural="Cursos"

class Alumnos(models.Model):
	Nombre = models.CharField(max_length=50)
	DNI = models.CharField(max_length=9)
	Direccion = models.CharField(max_length=60)
	CodPostal = models.CharField(max_length=5,verbose_name="Código postal")
	Localidad = models.CharField(max_length=30)
	Fecha_nacimiento = models.DateField('Fecha de nacimiento')
	Provincia = models.CharField(max_length=30)
	Unidad = models.ForeignKey(Cursos)
	Ap1tutor = models.CharField(max_length=20,verbose_name="Apellido 1 tutor")
	Ap2tutor = models.CharField(max_length=20,verbose_name="Apellido 2 tutor")
	Nomtutor = models.CharField(max_length=20,verbose_name="Nombre tutor")
	Telefono1 = models.CharField(max_length=12,blank=True)
	Telefono2 = models.CharField(max_length=12,blank=True)
	Obs=models.TextField(blank=True,verbose_name="Observaciones")

	def __unicode__(self):
		return self.DNI+" - "+self.Nombre

	class Meta:
		verbose_name="Alumno"
		verbose_name_plural="Alumnos"

