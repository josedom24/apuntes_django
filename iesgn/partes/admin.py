from django.contrib import admin
from partes.models import Cursos,Alumnos,Profesores,Departamentos,Partes

class AlumnosAdmin(admin.ModelAdmin):
    date_hierarchy = 'Fecha_nacimiento'
    actions_selection_counter=False
    list_filter = ['Unidad','Localidad']
admin.site.register(Cursos)
admin.site.register(Alumnos,AlumnosAdmin)
admin.site.register(Profesores)
admin.site.register(Departamentos)
admin.site.register(Partes)

# Register your models here.
