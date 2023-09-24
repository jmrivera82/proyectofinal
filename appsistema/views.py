
from django.shortcuts import render
from .models import Equipos, Personal, Compras, Trabajos

from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

#def obtenerAvatar(request):
#    avatares=Avatar.objects.filter(user=request.user.id)
#    if len(avatares)!=0:
#        return avatares[0].imagen.url
#    else:
#        return "/media/avatars/avatarpordefecto.jpg"

def inicio(request):
    return render(request,"appsistema/inicio.html")
    #Avatar=Avatar.objects.filter(user=request.user.id)[0].imagen.url    
    #return render(request,"appsistema/inicio.html", {"avatar":obtenerAvatar(request)})

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
    model=Equipos
    template_name="appsistema/equipo_detalle.html"
    
class EquipoUpdate(LoginRequiredMixin, UpdateView):
    model=Equipos
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

class ComprasList(ListView):
        model=Compras
        template_name="appsistema/compras.html"

class ComprasCreacion(LoginRequiredMixin, CreateView):
    model=Compras
    success_url=reverse_lazy("compras_list")
    fields=['numfactura','monto','descripcion','proveedor']

class ComprasDetalle(LoginRequiredMixin, DetailView):
    model=Compras
    template_name="appsistema/compras_detalle.html"

class TrabajosList(LoginRequiredMixin, ListView):
    model=Trabajos
    template_name="appsistema/trabajos.html"
    
class TrabajosCreacion(LoginRequiredMixin, CreateView):
    model=Trabajos
    success_url=reverse_lazy("trabajos_list")
    fields=['equipo', 'oficina', 'personal', 'descripcion', '', 'fecha_termino']
    
class TrabajosDetalle(LoginRequiredMixin, DetailView):
    model=Trabajos
    template_name="appsistema/trabajos_detalle.html"
    
class TrabajosDelete(LoginRequiredMixin, DeleteView):
    model=Trabajos
    success_url=reverse_lazy("trabajos_list")
    
class TrabajosUpdate(LoginRequiredMixin, UpdateView):
    model=Trabajos
    success_url=reverse_lazy("trabajos_list")    
    fields=['equipo', 'oficina', 'personal', 'descripcion', 'fecha_inicio', 'fecha_termino']
