from django import forms
from partes.models import Cursos

class UnidadForm(forms.Form):
    Unidad = forms.ModelChoiceField(queryset=Cursos.objects, empty_label=None)

