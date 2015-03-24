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
* raw_id_fields: Para indicar que un campo ForeignKey sea un text.
* readonly_fiels: Lista de campos de sólo lectura. Se puede indicar una función.
* save_as: Activar el save as... en el formulario de modificación. Para guardar como un nuevo objeto.
* save_on_top:_ Para poner la opción save arriba.
search_fields: Lista de campos, por los que se puedn buscar. Se puede configurar bastante (^,=,@)
* view_on_site: Controla el "View on site"

## Modificar plantillas

Más información:[Overriding admin templates](https://docs.djangoproject.com/en/1.7/ref/contrib/admin/#admin-overriding-templates)

* add_form_template
* change_form_template
* change_list_template
* delete_confirmation_template
* delete_selected_confirmation_template
* object_history_template

## Métodos

* save_model(request,obj,form.change): Puede hacer pre o post operaciones al salvar. No lo entiendo muy bien!!!
* delete_model(request, obj): Pre o post operaciones al borrar.
* save_formset(request, form, formset, change)
* get_ordering(request): Gestiona la ordenación.
* get_search_results(request, queryset, search_term): Modifica la lista de campos para la búsqueda.
* save_related(request, form, formsets, change)
* get_readonly_fields(request, obj=None)
* get_prepopulated_fields(request, obj=None)
* get_list_display(request)
* get_list_display_links(request, list_display)
* get_fields(request, obj=None)
* get_fieldsets(request, obj=None)
* get_list_filter(request)
* get_search_fields(request)
* get_inline_instances(request, obj=None)
* get_urls()
* get_form(request, obj=None, **kwargs)
* get_formsets(request, obj=None)
* get_formsets_with_inlines(request, obj=None)
* formfield_for_manytomany(db_field, request, **kwargs)
* formfield_for_choice_field(db_field, request, **kwargs)
* get_changelist(request, **kwargs)
* get_changelist_form(request, **kwargs)
* get_changelist_formset(request, **kwargs)
* has_add_permission(request)
* has_change_permission(request, obj=None)
* has_delete_permission(request, obj=None)
* get_queryset(request)
* get_paginator(queryset, per_page, orphans=0, allow_empty,first_page=True)
* response_add(request, obj, post_url_continue=None)
* response_change(request, obj)
* response_delete(request, obj_display)
* get_changeform_initial_data(request)
* add_view(request, form_url='', extra_context=None)
* change_view(request, object_id, form_url='', extra,context=None)
* changelist_view(request, extra_context=None)
* delete_view(request, object_id, extra_context=None)
* history_view(request, object_id, extra_context=None)

## Añadir CCS o javascript

		class Media:
        		css = {
            		"all": ("my_styles.css",)
        		}
        		js = ("my_code.js",)

## Añadiendo validación a medida

## InlineModelAdmin objects

Posibilidad de editar un modelo desde el formulario de otro. No lo veo interesante.

## Cambiar las plantillas 

## AdminSite

* site_header
* site_title
* index_title
* index_template
* app_index_template
* login_template
* login_form
* logout_template
* password_change_template
* password_change_done_template