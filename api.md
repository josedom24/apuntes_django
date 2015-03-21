# API del modelo

### Crear objetos (insert)

		from parte.models import Cursos
		c = Cursos(Abr='3', Curso='3º ESO')
		c.save()

### Modificar objeto (update)

		c.Curso="3 eso"
		c.save()

### Asignar campor ForeignKey y ManyToManyField

		c=Cursos.objects.get(Abr='2')
		a=Alumnos.objects.all()[1]
		a.Unidad=c
		a.save()
