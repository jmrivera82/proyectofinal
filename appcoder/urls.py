from django.urls import path
from .views import *

urlpatterns = [
    path("crear_curso/",crear_curso),
    path("listar_cursos/",listar_cursos),
    path("profesores/",profesores, name="profesores"),
    path("estudiantes/",estudiantes, name="estudiantes"),
    path("cursos/",cursos, name="cursos"),
    path("entregables/",entregables, name="entregables"),
    path("cursoFormulario/",cursoFormulario, name="cursoFormulario"),
    path("eliminarProfesor/<id>",eliminarProfesor, name="eliminarProfesor"),
    path("editarProfesor/<id>",editarProfesor, name="editarProfesor"),
    
    path("estudiante/list/", EstudianteList.as_view(),name="estudiante_list"),
    path("estudiante/nuevo/", EstudianteCreacion.as_view(),name="estudiante_crear"),
    path("estudiante/<pk>", EstudianteDetalle.as_view(),name="estudiante_detalle"),
    path("estudiante/borrar/<pk>", EstudianteEliminar.as_view(),name="estudiante_borrar"),

]
