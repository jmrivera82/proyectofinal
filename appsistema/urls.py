from django.urls import path
from .views import *

urlpatterns = [
path("inicio/",inicio, name="inicio"),
path("personal/",personal, name="personal"),
path("trabajos/",trabajos, name="trabajos"),
path("compras/",compras, name="compras"),
path("acercademi/",acercademi, name="acercademi"),

path("equipos/",equipos, name="equipos"),
path("equipos/list/", EquipoList.as_view(),name="equipos_list"),
path("equipos/crear/", EquipoCreacion.as_view(),name="equipos_crear"),


]