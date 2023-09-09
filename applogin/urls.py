from django.urls import path
from .views import *


urlpatterns = [
    #LOGIN LOGOUT REGISTER
    path("login/",login_request, name="login"),
    path("register/",register, name="register"),

]
