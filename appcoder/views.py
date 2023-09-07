from django.shortcuts import render
from .models import Estudiantes, Profesor, Entregable, Curso
from django.http import HttpResponse
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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

#def profesores(request):
#    if request.method=="POST":
#        #crea y guarda el objeto
#        pass
#    else:
#        #muestra el formulario vacio
#        profes=Profesor.objects.all()
#    return render(request,"appcoder/profesores.html", {"profes":profes})

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


def profesores (request):
    if request.method=="POST":
        form=profesorForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            profesion=info["profesion"]
            profesor=Profesor(nombre=nombre, apellido=apellido,email=email,profesion=profesion)
            profesor.save()
            mensaje="profesor creado"
            #return render(request,"appcoder/profesores.html",{"mensaje":mensaje,"formulario":formulario_profesor})
        else:        
            mensaje="datos inválidos"

        profesores=Profesor.objects.all() 
        formulario_profesor=profesorForm()
        return render(request, "appcoder/profesores.html",{"mensaje":mensaje,"formulario":formulario_profesor,"profesor":profesores})
    else:
        formulario_profesor=profesorForm()
        profesores=Profesor.objects.all() 

    return render (request,"appcoder/profesores.html",{"formulario":formulario_profesor,"profesores":profesores})

def eliminarProfesor(request, id):
    profesor=Profesor.objects.get(id=id)
    profesor.delete()
    profesores=Profesor.objects.all() 
    formulario_profesor=profesorForm()
    mensaje="profesor elimnado"
    return render(request, "appcoder/profesores.html",{"mensaje":mensaje,"formulario":formulario_profesor,"profesor":profesores})

def editarProfesor(request, id):
    profesor=Profesor.objects.get(id=id)

    if request.method=="POST":
        form=profesorForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            profesor.nombre=info["nombre"]
            profesor.apellido=info["apellido"]
            profesor.email=info["email"]
            profesor.profesion=info["profesion"]
            profesor.save()
            mensaje="profesor actualizado!!"
            profesores=Profesor.objects.all() 
            formulario_profesor=profesorForm()
            return render(request, "appcoder/profesores.html",{"mensaje":mensaje,"formulario":formulario_profesor,"profesor":profesores})
    
    else:
       # formulario_profesor=profesorForm(initial{"nombre"=profesor.nombre,"apellido"=profesor.apellido,"email"=profesor.email, "profesion"=profesor.profesion}) 
        return render(request, "appcoder/profesores.html",{"formulario":formulario_profesor,"profesor":profesor})

class EstudianteList(ListView):
        model=Estudiantes
        template_name="appcoder/estudiantes.html"
        
        
class EstudianteCreacion(CreateView):
    model=Estudiantes
    success_url=reverse_lazy("estudiante_list")
    fields=['nombre','comision','email']
    
class EstudianteDetalle(DetailView):
    model=Estudiantes
    template_name="appcoder/estudiante_detalle.html"
    
    
class EstudianteEliminar(DeleteView):
    model=Estudiantes
    success_url=reverse_lazy("estudiante_list")