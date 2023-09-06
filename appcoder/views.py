from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import *
# Create your views here.

def crear_curso(request):
    
    nombre_curso="programacion basica"
    comision_curso="48370"
    print("creando curso")
    curso=Curso(nombre=nombre_curso,comision=comision_curso)
    curso.save()
    respuesta=f"Curso creado:{curso.nombre} - {curso.comision}"
    return HttpResponse (respuesta)

def listar_cursos(request):
    cursos=Curso.objects.all()
    respuesta=""
    for curso in cursos:
            respuesta=f"{curso.nombre} - {curso.comision}<br>"
    return HttpResponse(respuesta)
    

def inicio(request):
    return render(request,"appcoder/inicio.html")

def profesores(request):
    if request.method=="POST":
        #crea y guarda el objeto
        pass
    else:
        #muestra el formulario vacio
        profes=Profesor.objects.all()
    return render(request,"appcoder/profesores.html", {"profes":profes})

def cursoFormulario(request):
    if request.method=="POST":
        nombre=request.POST["nombre"]
        comision=request.POST["comision"]
        curso=Curso(nombre=nombre,comision=comision)
        curso.save()
        return render(request, "appcoder/cursoFormulario.html",{"mensaje":"curso creado"})
    else:
        formulario_curso=cursoForm()
        return render(request,"appcoder/cursoFormulario.html", {"formulario":formulario_curso})

def estudiantes(request):
    return render(request,"appcoder/estudiantes.html")

def cursos(request):
    cursos=Curso.objects.all()
    return render(request,"appcoder/cursos.html", {"cursos":cursos})

def entregables(request):
    return render(request,"appcoder/entregables.html")
