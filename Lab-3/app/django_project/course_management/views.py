from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def asginatura(request):
	return render(request, 'asignatura.html')

def alumno(request):
	return render(request, 'alumno.html')