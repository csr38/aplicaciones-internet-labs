from django.shortcuts import render
from .models import Asignatura
from .models import Alumno
from .forms import AsignaturaForm 
from .forms import AlumnoForm


def index(request):
    asignaturas = Asignatura.objects.all()
    return render(request, 'index.html', {'asignaturas': asignaturas})

def asginatura(request):
    if request.method == 'POST':
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AsignaturaForm()

    asignaturas = Asignatura.objects.all()
    return render(request, 'asignatura.html', {'asignaturas': asignaturas, 'form': form})

def alumno(request):

    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AlumnoForm()

    alumnos = Alumno.objects.all()
    return render(request, 'alumno.html', {'alumnos': alumnos, 'form': form})
