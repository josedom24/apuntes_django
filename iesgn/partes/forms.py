from django import forms
from django.forms import ModelForm
from partes.models import Cursos,Partes

class UnidadForm(forms.Form):
	Unidad = forms.ModelChoiceField(queryset=Cursos.objects, empty_label=None)

class PartesForm(ModelForm):
		class Meta:
			model = Partes
            
