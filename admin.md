# Sitio de Administración

		from django.contrib import admin
		from partes.models import Alumnos

		class AlumnosAdmin(admin.ModelAdmin):
			...
		admin.site.register(Alumnos,AlumnosAdmin)

## Atributos de la clase ModelAdmin

* actions: Lista de funciones: [Admin actions](https://docs.djangoproject.com/en/1.7/ref/contrib/admin/actions/)
* actions_on_top,actions_on_bottom: Donde aparecen las lista de acciones.
* actions_selection_counter: Se ve o no el contador de acciones.
* date_hierarchy: Añader un navegador por un campo que sea Fecha.
* exclude: Lista de campos exclidos del formulario.
* field: Lista de campos que se incluyen en el formulario. Se puede configurar para que aparezcan varios campos en la misma línea.
* fieldsets: Controla el layout de add y change. Es una lista de dos tuplas donde se define los conjuntos de campos. ejemplo:
		fieldsets = (
		        (None, {
		            'fields': ('url', 'title', 'content', 'sites')
		        }),
		        ('Advanced options', {
		            'classes': ('collapse',),
		            'fields': ('enable_comments', 'registration_required', 'template_name')
		        }),
	En las opciondes de los campos puede sponer los siguientes claveS: fileds, classes, description.
* filter_horizonal: 