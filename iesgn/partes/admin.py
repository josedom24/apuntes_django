from django.contrib import admin
from partes.models import Cursos
from partes.models import Alumnos

class CursosAdmin(admin.ModelAdmin):
    fields = ['Abr', 'Curso']

admin.site.register(Cursos,CursosAdmin)
admin.site.register(Alumnos)

# Register your models here.
