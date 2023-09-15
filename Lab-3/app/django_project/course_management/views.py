from django.shortcuts import render, redirect
from .models import Asignatura
from .models import Alumno

def index(request):
    asignaturas = Asignatura.objects.all()
    return render(request, 'index.html', {'asignaturas': asignaturas})

def asginatura(request):
    asignaturas = Asignatura.objects.all()
    return render(request, 'asignatura.html', {'asignaturas': asignaturas})

def alumno(request):
    alumnos = Alumno.objects.all()
    asignaturas = Asignatura.objects.all()
    return render(request, 'alumno.html', {'alumnos': alumnos, 'asignaturas': asignaturas})

def registrarAsignatura(request):
    codigo = request.POST['codigo']
    nombre = request.POST['nombre']

    asignatura = Asignatura.objects.create(codigo=codigo, nombre=nombre)
    return redirect('/asignatura')

def registrarAlumno(request):
    nombre = request.POST['nombre']
    apellido_paterno = request.POST['apellido_paterno']
    apellido_materno = request.POST['apellido_materno']
    fecha_nacimiento = request.POST['fecha_nacimiento']
    # Obtén las asignaturas seleccionadas como una lista de IDs
    asignatura_ids = request.POST.getlist('asignaturas')

    # Crea una instancia de Alumno sin asignar las asignaturas
    alumno = Alumno.objects.create(
        nombre=nombre,
        apellido_paterno=apellido_paterno,
        apellido_materno=apellido_materno,
        fecha_nacimiento=fecha_nacimiento
    )

    # Ahora, asigna las asignaturas seleccionadas al alumno
    for asignatura_id in asignatura_ids:
        asignatura = Asignatura.objects.get(pk=asignatura_id)
        alumno.asignaturas.add(asignatura)

    return redirect('/alumno')

def eliminarAsignatura(request, id):
    asignatura = Asignatura.objects.get(id=id)
    asignatura.delete()
    return redirect('/asignatura')

def eliminarAlumno(request, id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    return redirect('/alumno')

def edicionAsignatura(request, id):
    asignatura = Asignatura.objects.get(id=id)
    return render(request, 'edicionAsignatura.html', {'asignatura': asignatura})

def edicionAlumno(request, id):
    alumno = Alumno.objects.get(id=id)
    asignaturas = Asignatura.objects.all()
    return render(request, 'edicionAlumno.html', {'alumno': alumno, 'asignaturas': asignaturas})

def editarAsignatura(request):
    id = request.POST['id']
    asignatura = Asignatura.objects.get(id=id)
    asignatura.codigo = request.POST['codigo']
    asignatura.nombre = request.POST['nombre']
    asignatura.save()
    return redirect('/asignatura')

def editarAlumno(request):
    id = request.POST['id']
    alumno = Alumno.objects.get(id=id)
    alumno.nombre = request.POST['nombre']
    alumno.apellido_paterno = request.POST['apellido_paterno']
    alumno.apellido_materno = request.POST['apellido_materno']
    alumno.fecha_nacimiento = request.POST['fecha_nacimiento']
    alumno.save()
    return redirect('/alumno')