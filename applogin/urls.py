from django.urls import path
from .views import register, login_request, editarperfil


urlpatterns = [
    #LOGIN LOGOUT REGISTER
    path("login/",login_request, name="login"),
    path("register/",register, name="register"),
    path("editarperfl/",editarperfil, name="editarperfil"),


]
