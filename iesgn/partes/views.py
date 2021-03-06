from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from partes.models import Alumnos
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from partes.forms import UnidadForm,PartesForm

# Create your views here.
@login_required(login_url='/partes/login')
def index(request):
	formulario = ""
	if request.method=='POST':
		formulario = request.POST["Unidad"]
		lista_alumnos = Alumnos.objects.filter(Unidad__id=request.POST["Unidad"])
		form = UnidadForm(request.POST)
	else:
		lista_alumnos = Alumnos.objects.filter(Unidad__id=1)
		form = UnidadForm()
	template = loader.get_template('index.html')
	context = RequestContext(request, {
 	    'lista_alumnos': lista_alumnos,'form':form
    })
	return HttpResponse(template.render(context))

def logout_view(request):
    logout(request)
    return redirect('/partes')

@login_required(login_url='/partes/login')
def amonestacion(request):
	if request.GET:
		datos={"Ida":request.GET["id"]}
		form=PartesForm(datos)
	template = loader.get_template('amonestacion.html')
	context = RequestContext(request, {'form':form.as_ul()})
	return HttpResponse(template.render(context))	