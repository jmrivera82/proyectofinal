from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from .forms import *
from .models import *

# Create your views here.

#def obtenerAvatar(request):
#    avatares=Avatar.objects.filter(user=request.user.id)
#    if len(avatares)!=0:
#        return avatares[0].imagen.url
#    else:
#        return "/media/avatars/avatarpordefecto.jpg"

#@login_required


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
    
    
@login_required
def editarperfil(request):
    usuario=request.user
    if request.method=='POST':
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data()
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "appsistema/inicio.html")
        else:
            return render(request, "applogin/editarperfil.html", {"form":form, "nombreusuario":usuario.username, "mensaje":f"nombre de usuario actualizado"})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "applogin/editarperfil.html", {"form":form, "nombreusuario":usuario.username, "mensaje":"DATOS INVÁLIDOS"})               