# Modelo de datos

La estructura del fichero donde definimos el modelo es el siguiente:

		from django.db import models
		
		class *nombre_tabla*(models.Model):
    		*nombre_campo* = models.*tipo_campo*(*opeciones_campo*)
    		...

    		# Función que nos permite representar un objeto de la clase
    		def __unicode__ (self):
    			return *nombre_campo*

    		# Metainformación del modleo
    		class Meta:
    			*lista_metainformación*

### Tipos de campo

* AutoField: Entero autonúmerico.