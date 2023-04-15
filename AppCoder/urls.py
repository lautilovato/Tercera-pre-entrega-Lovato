from django.urls import path
from .views import *


urlpatterns = [
    path('', inicio, name="inicio"),
    path('inicio/', inicioApp, name="inicioApp"),
    path('crear_curso/', crear_curso),
    path('crear_profesor/', crear_profesor),
    path('cursos/', cursos, name="cursos"),
    path('profesores/', profesores, name="profesores"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('busqueda_comision/', busqueda_comision, name="busqueda_comision"),
    path('buscar/', buscar, name= "buscar"),
]
