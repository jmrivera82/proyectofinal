
from django.shortcuts import render
from .models import Equipos, Personal, Compras, Trabajos

from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.


def inicio(request):
    return render(request,"appsistema/inicio.html")

@login_required
def trabajos(request):
    return render(request,"appsistema/trabajos.html")


def personal(request):
    return render(request,"appsistema/personal.html")

def acercademi(request):
    return render(request,"appsistema/acercademi.html")

@login_required
def compras(request):
    return render(request,"appsistema/compras.html")

def equipos(request):
    return render(request,"appsistema/equipos.html")

class EquipoList(ListView):
        model=Equipos
        template_name="appsistema/equipos.html"

class EquipoCreacion(LoginRequiredMixin, CreateView):
    model=Equipos
    success_url=reverse_lazy("equipos_list")
    fields=['codigoint','tipo','descripcion','marca','estado']

class EquipoDetalle(LoginRequiredMixin, DetailView):
    model=Personal
    template_name="appsistema/equipo_detalle.html"
    
class EquipoUpdate(LoginRequiredMixin, UpdateView):
    model=Personal
    success_url=reverse_lazy("equipo_list")    
    fields=['codigoint','tipo','descripcion','marca','estado']

class PersonalList(LoginRequiredMixin, ListView):
    model=Personal
    template_name="appsistema/personal.html"
    
class PersonalCreacion(LoginRequiredMixin, CreateView):
    model=Personal
    success_url=reverse_lazy("personal_list")
    fields=['nombre', 'direccion', 'ciudad', 'fecha_ingreso', 'email', 'telefono']
    
class PersonalDetalle(LoginRequiredMixin, DetailView):
    model=Personal
    template_name="appsistema/personal_detalle.html"
    
class PersonalDelete(LoginRequiredMixin, DeleteView):
    model=Personal
    success_url=reverse_lazy("personal_list")
    
class PersonalUpdate(LoginRequiredMixin, UpdateView):
    model=Personal
    success_url=reverse_lazy("personal_list")    
    fields=['nombre', 'direccion', 'ciudad', 'fecha_ingreso', 'email', 'telefono']


 