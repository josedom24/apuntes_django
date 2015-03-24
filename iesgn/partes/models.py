# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Cursos(models.Model):
	
	Curso = models.CharField(max_length=30)

	def __unicode__(self):
		return self.Curso

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

class Departamentos(models.Model):
	Abr = models.CharField(max_length=4)
	Nombre = models.CharField(max_length=30)

	def __unicode__(self):
		return self.Nombre

	class Meta:
		verbose_name="Departamento"
		verbose_name_plural="Departamentos"


class Profesores(models.Model):
	Nombre = models.CharField(max_length=20)
	Apellidos = models.CharField(max_length=30)
	Telefono = models.CharField(max_length=9,blank=True)
	Movil = models.CharField(max_length=9,blank=True)
	Email = models.EmailField()
	Departamento = models.ForeignKey(Departamentos)
	Baja = models.BooleanField(default=False)
	Ce = models.BooleanField(default=False,verbose_name="Consejo Escolar")
	Etcp = models.BooleanField(default=False)
	Tic = models.BooleanField(default=False)
	Bil = models.BooleanField(default=False,verbose_name="Bilingüe")
	Tutor = models.ForeignKey(Cursos)

	def __unicode__(self):
		return self.Nombre+" "+self.Apellidos

	class Meta:
		verbose_name="Profesor"
		verbose_name_plural="Profesores"


class Partes(models.Model):
	tipo = (
    ('a', 'Amonestación'),
    ('c', 'Citación'),
    ('s', 'Sanción'),
    )

	hora = (
		('1','Primera'),
		('2','Segunda'),
		('3','Tercera'),
		('4','Recreo'),
		('5','Cuarta'),
		('6','Quinta'),
		('7','Sexta'),

	)
	dict_tipo={'a':'Amonestacion','c':'Citacion','s':'Sancion'}

	Ida = models.ForeignKey(Alumnos)
	Tipo = models.CharField(max_length=1,choices=tipo,default='a')
	Fecha = models.DateField()
	Fecha_fin = models.DateField()
	Hora = models.CharField(max_length=1,choices=hora,default='1')
	Sancion = models.CharField(max_length=100,blank=True)
	Comentario=models.TextField(blank=True)
	Profesor = models.ForeignKey(Profesores)

	def __unicode__(self):
		return self.Ida.Nombre + "(" + self.dict_tipo[self.Tipo] + ")"

	class Meta:
		verbose_name="Parte"
		verbose_name_plural="Partes"

class AltaMasiva(models.Model):
		Fichero=models.FileField(upload_to='documents/%Y/%m/%d')