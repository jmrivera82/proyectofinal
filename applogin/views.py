from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import *

# Create your views here.

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu,password=clave)
            if usuario is not None:
                login(request,usuario)
                return render (request, "appsistema/inicio.html", {"mensaje":f"Bienvenido Usuario {usu}"})
            else:
                return render(request,"applogin/login.html", {"form":form, "mensaje": "Datos invalidos"})
            
        else:
            return render(request,"applogin/login.html", {"form":form, "mensaje": "Datos invalidos"})
    else:
        form=AuthenticationForm()
        return render (request, "applogin/login.html", {"form":form})
    

def register(request):
    if request.method=="POST":
        form=registrousuarioForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre_usuario=info["username"]
            form.save()
            return render(request,"appsistema/inicio.html",{"mensaje":f"usuario {nombre_usuario} creado correctamente"})
        else:
            return render(request,"applogin/register.html",{"form":form,"mensaje":f"datos mal ingresados"})

    else:
        form=registrousuarioForm()
        return render(request,"applogin/register.html", {"form":form})