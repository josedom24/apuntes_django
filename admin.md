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
* filter_horizonal,filetr_vertical: Cómo se comportan los campos ManyToManyField.
* form: Puedo usar o modificar los formularios add / change.
* formfield_overrides: Puedo cambiar las opciones de los campos de los formularios.
* inlines: Ver [InlineModelAdmin](https://docs.djangoproject.com/en/1.7/ref/contrib/admin/#django.contrib.admin.InlineModelAdmin)
* list_display: La lista de atributos que aprece en la lista de registro. Se puede indicar la salida de una función.
* list_display_links: Cúal de los atributos de list_display, tiene un link, para ser editado.
* list_editable: Lista de los campos editables en la página donde se muestra los datos.
* list_filter: Activa filtros en el lateral. Lista de campos para los filtros. Puedo crear mis propios filtros.
* list_max_show_all: Número de registro para mostrar un botón "Show all".
* list_per_page: Número de registro por página.
* list_select_related: 
* ordering: Gestiona la ordenación.
* paginator: Paginador.
* prepopulated_fields: 
preserve_filters: Para recordar los filtros.
* radio_fields: Para indicar que un campo ForeignKey sea un radio.
* raw_id_fields