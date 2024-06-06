"""TFG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Plazeduca.views import anadir_cita, anadir_trabajo_profesor, asignaturasProfesor, base, incidencias_alumnos, incidenciasAlumno, inicio,cerrarS, mostrarCalendario, notasProfesor, trabajosProfesor,tutorCurso, asignaturas,notasAlumno,trabajosAlumno,encuesta, tutorCurso, tutoriaClase
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio,name="login"),
    path('base',base,name="base"),
    path('cerrarSesion',cerrarS,name="cerrar"),
    path('asignaturas',asignaturas,name="asignaturas"),
    path('notas',notasAlumno,name="notasAl"),
    path('trabajos',trabajosAlumno,name="trabajosAl"),
    path('encuesta',encuesta,name="encuesta"),
    path('incidencias',incidenciasAlumno,name="incidencias"),
    path('tutor',tutorCurso,name="tutoria"),
    path('reunion',anadir_cita,name="cita"),
    path('trabajosMandados',trabajosProfesor,name="trabajosProf"),
    path('asignaturasProfesor',asignaturasProfesor,name="asignaturasProf"),
    path('notasSubidas',notasProfesor,name="notasProf"),
    path('alumnosTutoria',tutoriaClase,name="alumnosTutoria"),
    path('anadirTrabajo',anadir_trabajo_profesor,name="anadirTrabajo"),
    path('incidenciasAlumnos',incidencias_alumnos,name="incidenciasAlumnos"),
    path('calendario',mostrarCalendario,name="calendario")
]
