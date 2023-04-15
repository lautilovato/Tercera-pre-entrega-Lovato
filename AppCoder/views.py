from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def crear_curso(request):
    
    nombre_curso= "Marketing"
    comision_curso= 918052

    curso= Curso(nombre= nombre_curso, comision= comision_curso)
    curso.save()
    respuesta= f"Curso creado: {nombre_curso} - {comision_curso}"
    return HttpResponse(respuesta)

def crear_profesor(request):
    
    nombre_profesor= "Franco"
    apellido_profesor= "Di Martino"
    email_profesor = "fdm@gmail.com"
    profesion_profesor = "docente"

    profesor= Profesor(nombre= nombre_profesor, apellido= apellido_profesor, email = email_profesor, profesion = profesion_profesor )
    profesor.save()
    respuesta= f"profesor creado: {nombre_profesor} - {apellido_profesor}"
    return HttpResponse(respuesta)

def cursos(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = Curso()
            curso.nombre = form.cleaned_data["nombre"]
            curso.comision = form.cleaned_data["comision"]
            curso.save()
            form = CursoForm()
    else:
            form = CursoForm()

    cursos = Curso.objects.all()
    contexto = {"cursos" : cursos, "form" : form}
    return render(request, "AppCoder/cursos.html", contexto)
        
 
def profesores(request):
    
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            profesor = Profesor()
            profesor.nombre = form.cleaned_data["nombre"]
            profesor.apellido = form.cleaned_data["apellido"]
            profesor.email = form.cleaned_data["email"]
            profesor.profesion = form.cleaned_data["profesion"]
            profesor.save()
            form = ProfesorForm()
    else:
            form = ProfesorForm()

    profesores = Profesor.objects.all()
    contexto = {"profesores" : profesores, "form" : form}
    return render(request, "AppCoder/profesores.html", contexto)

def estudiantes(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            estudiante = Estudiante()
            estudiante.nombre = form.cleaned_data["nombre"]
            estudiante.apellido = form.cleaned_data["apellido"]
            estudiante.email = form.cleaned_data["email"]
            estudiante.save()
            form = EstudianteForm()
    else:
            form = EstudianteForm()

    estudiantes = Estudiante.objects.all()
    contexto = {"estudiantes" : estudiantes, "form" : form}
    return render(request, "AppCoder/estudiantes.html", contexto)

def entregables(request):
    return render(request, "AppCoder/entregables.html")

def inicio(request):
    return render(request, "AppCoder/inicioPrincipal.html")

def inicioApp(request):
    return render(request, "AppCoder/inicio.html")

def busqueda_comision(request):
    return render(request, "AppCoder/busqueda_comision.html")

def buscar(request):
    
    comision= request.GET["comision"]
    if comision!="":
        cursos= Curso.objects.filter(comision__icontains=comision)#buscar otros filtros en la documentacion de django
        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos": cursos})
    else:
        return render(request, "AppCoder/busquedaComision.html", {"mensaje": "Esta comision no existe."})