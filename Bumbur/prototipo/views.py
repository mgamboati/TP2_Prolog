from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render_to_response('initializr.html')

def mantenimiento(request):
	return render_to_response('mantenimiento.html')

def consultar(request):
	return render_to_response('consultar.html')

def respuesta(request):
	return HttpResponse("El restaurante es Mac Donalds")