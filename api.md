# API del modelo

### Crear objetos (insert)

		from parte.models import Cursos
		c = Cursos(Abr='3', Curso='3º ESO')
		c.save()

### Modificar objeto (update)

		c.Curso="3 eso"
		c.save()

### Asignar campos ForeignKey y ManyToManyField

		c=Cursos.objects.get(Abr='2')
		a=Alumnos.objects.all()[1]
		a.Unidad=c
		a.save()

Para añadir un objeto a una relación N-N hay que utilizar el método add. cuando haga un ejemplo lo pongo aquí.

### Obtener objetos (select)

**QuerySet**: representa un conjunto de objetos, registros de una base de datos. En SQL un select.
**filter**: Me permite realizar las clausulas where y limit de SQL.
**manager**: Me permite obtener QuerySet, por defecto tengo objects.

### Obtener todos los objetos

Similar a:

		select * from alumnos

		lista=Alumnos.objects.all()

Lista es del tipo QuerySet.