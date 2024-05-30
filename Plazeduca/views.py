from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render
from Plazeduca.forms import Login
from Plazeduca.models import Alumnos, Asignaturas, Notas, Profesor, Trabajos


def inicio(request):
    if request.method=='POST':
        my_frm=Login(request.POST)
        if my_frm.is_valid():
            alum=buscar_alumno(my_frm)
            if(alum!=None):
                request.session['logueado']={"dni":alum.dni}
                return redirect('base')
            else:
                return render(request,'login.html',{'form':my_frm,'mensaje':"Nombre de usuario o contraseña incorrecto"})
    else:
        my_frm=Login()
    return render(request,'login.html',{'form':my_frm})
    
def base(request):
    perfil=buscar_alumno_dni(request)
    return render(request,'contenidoAlumno.html',{"sesion":request.session["logueado"]["dni"],"perfil":perfil})

def notasAlumno(request):
    notas=notas_al(request)
    perfil=buscar_alumno_dni(request)
    return render(request,'contenidoNotas.html',{"sesion":request.session["logueado"]["dni"],"notasAlumno":notas,"perfil":perfil})

def trabajosAlumno(request):
    trabajos=trabajos_al(request)
    perfil=buscar_alumno_dni(request)
    return render(request,'contenidoTrabajos.html',{"sesion":request.session["logueado"]["dni"],"trabajosAlumno":trabajos,"perfil":perfil})

def asignaturas(request):
    asig=buscarAsignaturas(request)
    perfil=buscar_alumno_dni(request)
    return render(request,'contenidoAsignaturas.html',{"asig":asig,"perfil":perfil})

def cerrarS(request):
    logout(request)
    return redirect('login')


def buscarAsignaturas(request):
    alum=buscar_alumno_dni(request)
    try:
        asig=Asignaturas.objects.get_queryset().filter(curso=alum.cursos)
    except Asignaturas.DoesNotExist:
        return None
    else:
        return asig
        

def tutor(request):
    tutor=buscar_tutor(request)
    return render(request,'tutor.html',{"tutor":tutor})

def buscar_alumno(my_frm):
    try:
        alum=Alumnos.objects.get(usuario=my_frm.cleaned_data["usuario"],password=my_frm.cleaned_data["contrasena"])
    except Alumnos.DoesNotExist:
            return None
    else:
        return alum
    
def buscar_alumno_dni(request):
    try:
        alum=Alumnos.objects.get(dni=request.session["logueado"]["dni"])
    except Alumnos.DoesNotExist:
            return None
    else:
        return alum

def buscar_tutor(request):
    try:
        alum=buscar_alumno_dni(request)
        tutor=Profesor.objects.get(tutoria=alum.cursos)
    except Profesor.DoesNotExist:
            return None
    else:
        return tutor
        
    
    
def notas_al(request):
    try:
        notas=Notas.objects.get_queryset().filter(dni_alumno=request.session["logueado"]["dni"])
    except Notas.DoesNotExist:
            return None
    else:
        return notas
    
def trabajos_al(request):
    
    try:
        notas=Trabajos.objects.get_queryset().filter(dni_alumnos=request.session["logueado"]["dni"])
    except Notas.DoesNotExist:
            return None
    else:
        return notas
    
def encuesta(request):
    perfil=buscar_alumno_dni(request)
    return render(request,'contenidoEncuesta.html',{"perfil":perfil})
