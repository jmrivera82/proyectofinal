
from django.shortcuts import render
from .models import Equipos, Personal, Compras, Trabajos

from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


def inicio(request):
    return render(request,"appsistema/inicio.html")


def trabajos(request):
    return render(request,"appsistema/trabajos.html")

def personal(request):
    return render(request,"appsistema/personal.html")

def acercademi(request):
    return render(request,"appsistema/acercademi.html")

def compras(request):
    return render(request,"appsistema/compras.html")

def equipos(request):
    return render(request,"appsistema/equipos.html")

class EquipoList(ListView):
        model=Equipos
        template_name="appsistema/equipos.html"

class EquipoCreacion(CreateView):
    model=Equipos
    success_url=reverse_lazy("equipos_list")
    fields=['codigoint','producto','tipo','descripcion','marca']




 