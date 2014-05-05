from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
import backEnd

#Vista al template de la pagina de inicio
def home(request):
	#backEnd.main()
	return render_to_response('home.html')

#Definicion de la clase restaurantes para el uso de una form
class restaurante(forms.Form):
	Nombre = forms.CharField(max_length=100)
	Tipo_de_comida = forms.CharField(max_length=100)
	Ubicacion = forms.CharField(max_length=100)
	Telefono = forms.CharField(max_length=100)
	Horario = forms.CharField(max_length=100)

#Vista al template de la pagina de mantenimiento de datos
def mantenimiento(request):
	if request.method == 'POST':
		form = restaurante(request.POST)
		if form.is_valid():
			#si los datos son validos, bound-earlos y obtenerlos para insertarlos
			nombre = form.cleaned_data['Nombre']
			tipo = form.cleaned_data['Tipo_de_comida']
			horario = form.cleaned_data['Horario']
			ubicacion = form.cleaned_data['Ubicacion']
			telefono = form.cleaned_data['Telefono']
			#backEnd.nuevoRestaurante(nombre, tipo, ubicacion, telefono, horario, "bigMac") #platillos favoritos
			#print "El nuevo restaurante es: "+nombre+"  "+tipo_de_comida+"  "+ubicacion+"  "+telefono+"  "+horario
			return render_to_response('felicidades.html')
	else:
		form = restaurante()
	return render(request, 'mantenimiento.html', {
        'form': form,
    })

#Vista al template de la pagina de consultar datos
def consultar(request):
	return render_to_response('consultar.html')

#Definicion de la clase platillos para el uso de una form
class platillos(forms.Form):
	Nombre = forms.CharField(max_length=100)
	Tipo_de_comida = forms.CharField(max_length=100)
	Pais_de_origen = forms.CharField(max_length=100)
	Lista_Ingredientes = forms.CharField(max_length=200)

#Vista al template de la pagina de consultar datos
def platillo(request):
	if request.method == 'POST':
		form = platillos(request.POST)
		if form.is_valid():
			#si los datos son validos, bound-earlos y obtenerlos para insertarlos
			nombre = form.cleaned_data['Nombre']
			tipo = form.cleaned_data['Tipo_de_comida']
			pais = form.cleaned_data['Pais_de_origen']
			ingredientes = form.cleaned_data['Lista_Ingredientes']
			#backEnd.nuevoRestaurante(nombre, tipo, ubicacion, telefono, horario, "bigMac") #platillos favoritos
			#print "El nuevo restaurante es: "+nombre+"  "+tipo_de_comida+"  "+ubicacion+"  "+telefono+"  "+horario
			return render_to_response('felicidades.html')
	else:
		form = platillos()
	return render(request, 'platillo.html', {
        'form': form,
    })

def respuesta(request):
	return HttpResponse("El restaurante es Mac Donalds")
