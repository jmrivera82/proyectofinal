from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
path("inicio/",inicio, name="inicio"),
path("personal/",personal, name="personal"),
path("trabajos/",trabajos, name="trabajos"),
path("compras/",compras, name="compras"),
path("acercademi/",acercademi, name="acercademi"),

path("equipos/",equipos, name="equipos"),
path("equipos/list/", EquipoList.as_view(),name="equipos_list"),
path("equipos/crear/", EquipoCreacion.as_view(),name="equipos_crear"),
path("equipos/<pk>", EquipoDetalle.as_view(),name="equipo_detalle"),
path("equipos/editar/<pk>", EquipoUpdate.as_view(),name="equipo_editar"),

path("personal/list/", PersonalList.as_view(),name="personal_list"),
path("personal/nuevo/", PersonalCreacion.as_view(),name="personal_crear"),
path("personal/<pk>", PersonalDetalle.as_view(),name="personal_detalle"),
path("personal/borrar/<pk>", PersonalDelete.as_view(),name="personal_borrar"),
path("personal/editar/<pk>", PersonalUpdate.as_view(),name="personal_editar"),

path("compras/list/", ComprasList.as_view(),name="compras_list"),
path("compras/nuevo/", ComprasCreacion.as_view(),name="compras_crear"),
path("compras/<pk>", ComprasDetalle.as_view(),name="compras_detalle"),

path("trabajos/list/", TrabajosList.as_view(),name="trabajos_list"),
path("trabajos/crear/", TrabajosCreacion.as_view(),name="trabajos_crear"),
path("trabajos/<pk>",TrabajosDetalle.as_view(),name="trabajos_detalle"),
path("trabajos/borrar/<pk>", TrabajosDelete.as_view(),name="trabajos_borrar"),
path("trabajos/editar/<pk>", TrabajosUpdate.as_view(),name="trabajos_editar"),

path("logout/", LogoutView.as_view(), name='logout'),

path('busquedaTrabajo/',busquedaTrabajo,name='busquedaTrabajo'),
path('buscar/',buscar),

]