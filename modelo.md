# Modelo de datos

La estructura del fichero donde definimos el modelo es el siguiente:

		from django.db import models
		
		class *nombre_tabla*(models.Model):
    		*nombre_campo* = models.*tipo_campo*(*opeciones_campo*)