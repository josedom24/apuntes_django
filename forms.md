# Formularios

		from django import forms

		class NameForm(forms.Form):
    		your_name = forms.CharField(label='Your name', max_length=100)

La vista:

		from django.shortcuts import render
		from django.http import HttpResponseRedirect		

		def get_name(request):
		    # if this is a POST request we need to process the form data
		    if request.method == 'POST':
		        # create a form instance and populate it with data from the request:
		        form = NameForm(request.POST)
		        # check whether it's valid:
		        if form.is_valid():
		            # process the data in form.cleaned_data as required
		            # ...
		            # redirect to a new URL:
		            return HttpResponseRedirect('/thanks/')		

		    # if a GET (or any other method) we'll create a blank form
		    else:
		        form = NameForm()		

		    return render(request, 'name.html', {'form': form})

La plantilla:

		<form action="/your-name/" method="post">
		    {% csrf_token %}
		    {{ form }}
		    <input type="submit" value="Submit" />
		</form>

* form bound: Tiene datos, se puede validar.
* form unbound: No tiene información

Crear un formaulario:

		f = ContactForm()

Llenar datos den un formulario desde un diccionario:

 		f = ContactForm(data)


## Gestión de errores

* is_bound: True si el formulario tiene datos.
* clean(): 
* is_valid(): True si el formulario es válido.
* errors: Diccionario de los mensajes de error. La clave es el nombre del campo. Los mensajes son una lista, porque un campo puede tener varios mensajes de errores.
* errors.as_data(): diccionario de los campos con el objeto ValidationError.
* errors.as_json()
* add_error(): Añade nuevos errores.
* non_field_errors():

## Valores iniciales

* initial: valores iniciales del formulario.

 		f = ContactForm(initial={'subject': 'Hi there!'}) 

## Comprobando si los valores han cambiado

 * has_changed(): True, si los datos de request.POST son diferentes a initial.

## Accediendo a los campos del formulario

 * fields: Valores del formulario.
 Ejemplos:

 		for row in f.fields.values(): print(row)
 		f.fields['name']
 		f.fields['name'].label = "Username"

## Accediendo al los datos "válidos" (clean)

* cleaned_data: Una vez que es válido el formulario, los datos para su procesamiento se pueden obtener de este diccionario.

## Salida HTML del formulario

