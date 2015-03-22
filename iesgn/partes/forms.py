from django.forms import ModelForm
from partes.models import Alumnos

class UnidadForm(ModelForm):
    class Meta:
        model = Alumnos
        fields = ['Unidad']
    

