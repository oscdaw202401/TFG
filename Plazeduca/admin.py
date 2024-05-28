from django.contrib import admin
from .models import Alumnos,Asignaturas,Asistencias,Citas,Cursos,Notas,Profesor,Trabajos,Administrador
# Register your models here.

class AlumnoAdmin(admin.ModelAdmin):
    list_display=("dni","usuario","email","telefono","fecha_nac","faltas","retrasos")
    list_filter=("usuario","fecha_nac","dni")
    fields=["dni",("usuario","password"),("nombre","apellidos"),"direccion","email","telefono","cursos",("fecha_nac"),("faltas","retrasos")]

admin.site.register(Alumnos, AlumnoAdmin)


class AsignaturaAdmin(admin.ModelAdmin):
    list_display=("nombre","profesor","horas_semanales","curso")
    list_filter=("curso","nombre")
    
admin.site.register(Asignaturas,AsignaturaAdmin)


class AsistenciaAdmin(admin.ModelAdmin):
    list_display=("dni_alumnos","num_faltas","num_retrasos","nom_asignatura")
    list_filter=("dni_alumnos","nom_asignatura")
    
    
    
admin.site.register(Asistencias,AsistenciaAdmin)


class CitaAdmin(admin.ModelAdmin):
    list_display=("dni_profesor","dni_alumnos","motivo","fecha_envio")
    list_filter=("dni_profesor","dni_alumnos","fecha_envio")
    
admin.site.register(Citas,CitaAdmin)


class CursoAdmin(admin.ModelAdmin):
    list_display=("nombre","siglas")
    list_filter=("nombre","siglas")
    
admin.site.register(Cursos,CursoAdmin)


class NotaAdmin(admin.ModelAdmin):
    list_display=("nota","dni_alumno","nom_asignatura","fecha_subida")
    list_filter=("dni_alumno","nom_asignatura","fecha_subida")
    
admin.site.register(Notas,NotaAdmin)


class ProfesorAdmin(admin.ModelAdmin):
    list_display=("dni","usuario","email","telefono","fecha_nac","cursos","tutoria")
    list_filter=("dni","usuario","cursos","tutoria")
    fields=["dni",("usuario","password"),("nombre","apellidos"),"telefono","fecha_nac","direccion","email",("cursos","tutoria")]

admin.site.register(Profesor,ProfesorAdmin)


class TrabajoAdmin(admin.ModelAdmin):
    list_display=("trabajo","dni_alumnos","nom_asignatura","fecha_inicio","fecha_entrega")
    list_filter=("dni_alumnos","nom_asignatura","fecha_inicio","fecha_entrega")
    
admin.site.register(Trabajos,TrabajoAdmin)

    
admin.site.register(Administrador)