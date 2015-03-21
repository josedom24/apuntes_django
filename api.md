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

* **QuerySet**: representa un conjunto de objetos, registros de una base de datos. En SQL un select.
* **filter**: Me permite realizar las clausulas where y limit de SQL.
* **manager**: Me permite obtener QuerySet, por defecto tengo objects.

### Obtener todos los objetos

Similar a: **select * from alumnos**
		
		lista=Alumnos.objects.all()

Lista es del tipo QuerySet.

### Obtener varios objetos (select-where)

* **filter**: Devuelve objetos cuyo parámetros de búsqueda coinciden.
* **exclude**: Devuelve objetos cuyo parámetros de búsqueda no coinciden.

select * from Alumnos where CodPostal='41710'
	
		lista=Alumnos.objects.filter(CodPostal='41710')

select * from Alumnos where Provincia!='Sevilla'

		lista=Alumnos.objects.exclude(Provincia='Sevilla')

Se pueden concatenar: Alumnos.objects.filter(...).exclude(...).filter(...)


### Obtener un objeto (select-where)

Si quieres obtener un sólo registro, por ejemplo preguntando por la clave primaria:

		 a=Alumnos.objects.get(id=1)

Si no obtienes ningún registro, salta la excepción DoesNotExist, si devuelve más de un registro, salta la excepción MultipleObjectsReturned.

### Limitando resultados (limit)

Un querySet es una lista de objetos, por lo tanto se pueden seleccionar como lo hacemos con las listas:

		a=Alumnos.objects.all()[1:5]

### Realizando consultas

Para los metodos get(), filter() y exclude()

		metodo(campo__operador)

Operadores:

* exact: Coincidencia exacta, es lo mismo:

		Alumnos.objects.filter(Nombre__exact='Jose')
		Alumnos.objects.filter(Nombre='Jose')

* iexact: Coincidencia exacta, sin tener en cuenta mayúsculas y minúsculas.
* constains: Contiene el valor, como LIKE '%...%'
* startswith, endswith
* iconstains,istartswith, iendswith: Igual que las anteriores, sin tener en cuenta mayúsculas y minúsculas.
* lte,lt,gte,gt
* in: está en una lista


### JOIN

		lista=Alumnos.objects.filter(Unidad__Abr='1')

Hay que estudiarlo con más detenimiento, cuando me haga falta.

### F()

### pk

Para identificar a la clave primaria puedo usar pk.

### Q()

Me permite hacer consultas usando el operador OR.


### Comparando objetos

==

### Borrando objetoas

		a.delete()

### Modificar varios objetos

update

