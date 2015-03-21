# Modelo de datos

Cada vez que cambiamos el modelo, podemos crear una migración, sincronizar con la base de datos y crear la API del modelo:

		python manage.py makemigrations
		python manage.py migrate

La estructura del fichero donde definimos el modelo es el siguiente:

		from django.db import models
		
		class *nombre_tabla*(models.Model):
    		*nombre_campo* = models.*tipo_campo*(*opeciones_campo*)
    		...

    		# Función que nos permite representar un objeto de la clase
    		def __unicode__ (self):
    			return self.*nombre_campo*

    		# Metainformación del modleo
    		class Meta:
    			*lista_metainformación*

### Tipos de campo

* AutoField: Entero autonúmerico.
* BigIntergerField
* BinaryField
* BooleanField
* CharField(max_length=None)
* CommaSeparatedIntegerField(max_length=None)
* DateField(auto_now=False,auto_now_add=False)
* DateTimeField(auto_now=False,auto_now_add=False)
* DecimealField(max_digits=None,decimal_places=None)
* EmailField(max_length=75)
* FileField(uptoad_to=None,max_length=100)
* FilePathField
* FloatField
* ImageField(upload_to=None,height_field=None,width_field=None,max_length=None)
* IntegerField
* IPAddressField
* GenericIPAddressField
* NullBooleanField
* PositiveIntegerField
* PositiveSmallIntegerField
* SlugField(max_length=50)
* SmallIntegerField
* TextField
* TimeField
* URLField(max_length=200)


### Campos de relación

* ForeigKey (othermodel)

	* Para hacer una realción recursiva: FroreigKey('self')
	* Si el modelo está en otra aplicación: ForeigKey(app.othermodel)

	Parámetros:

	* limit_choice_to
	* related_name
	* related_query_name
	* to_field
	* db_constraint
	* on_delete 
	* swappable

* ManyToManyField(othermodel)

	Parámetros:

	* limit_choice_to
	* related_name
	* related_query_name 
	* symmetrical
	* through
	* through_fields
	* db_table
	* db_constraint
	* swappable

* OneToOneField(othermodel,parent_link=flase)

Los mismos parámetros que le campo ForeigKey,

### Opciones de los campos

* null
* blank: Campo no requerido (True)
* choice
* db_column
* db_index
* db_tablespace
* default
* editable
* error_messages
* help_text
* primmary_key
* unique
* unique_for_date
* unique_for_month
* unique_for_year
* verbose_name
* validators

### Metainformación en los modelos

* abstract
* app_label
* db_table
* db_tablespace
* get_lastest_by
* managed
* order_with_respect_to
* ordering
* permissions
* default_permissions
* proxy
* select_on_save
* unique_together
* index_together
* verbose_name: Nombre "humano" singular.
* verbose_name_prural: Nombre "humano" plural.

