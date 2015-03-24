from django.contrib import admin
from partes.models import Cursos,Alumnos,Profesores,Departamentos,Partes
from django.utils.html import format_html
class AlumnosAdmin(admin.ModelAdmin):
    date_hierarchy = 'Fecha_nacimiento'
    actions_selection_counter=False
    list_filter = ['Unidad','Localidad']
    list_display = ["Nombre",'DNI',"Unidad","Telefono1","enlace"]
    list_display_links = ["Nombre",'DNI']
    list_editable = ["Telefono1"]
    search_fields = ['Nombre','DNI']

    def enlace(self,obj):
   		return format_html('<a href="#">Enlace</a>')

admin.site.register(Cursos)
admin.site.register(Alumnos,AlumnosAdmin)
admin.site.register(Profesores)
admin.site.register(Departamentos)
admin.site.register(Partes)

# Register your models here.
