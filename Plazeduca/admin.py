from django.contrib import admin
from .models import Alumnos,Asignaturas,Cursos,Profesor,Administrador
# Register your models here.

class AlumnoAdmin(admin.ModelAdmin):
    list_display=("dni","usuario","email","telefono","fecha_nac")
    list_filter=("usuario","fecha_nac","dni")
    fields=["dni",("usuario","password"),("nombre","apellidos"),"direccion","email","telefono","cursos",("fecha_nac")]

admin.site.register(Alumnos, AlumnoAdmin)

class AsignaturaAdmin(admin.ModelAdmin):
    list_display=("nombre","profesor","horas_semanales","curso")
    list_filter=("curso","profesor")
    
admin.site.register(Asignaturas,AsignaturaAdmin)

class CursoAdmin(admin.ModelAdmin):
    list_display=("nombre","siglas")
    list_filter=("nombre","siglas")
    
admin.site.register(Cursos,CursoAdmin)

class ProfesorAdmin(admin.ModelAdmin):
    list_display=("dni","usuario","email","telefono","fecha_nac","cursos","tutoria")
    list_filter=("dni","usuario","cursos","tutoria")
    fields=["dni",("usuario","password"),("nombre","apellidos"),"telefono","fecha_nac","direccion","email",("cursos","tutoria")]

admin.site.register(Profesor,ProfesorAdmin)
    
admin.site.register(Administrador)