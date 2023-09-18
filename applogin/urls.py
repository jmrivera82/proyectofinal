from django.urls import path
from .views import register, login_request, editarperfil

from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    #LOGIN LOGOUT REGISTER
    path("login/",login_request, name="login"),
    path("register/",register, name="register"),
    path("editarperfl/",editarperfil, name="editarperfil"),


]

