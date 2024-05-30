import datetime
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from Plazeduca.forms import CitaForm, Login
from Plazeduca.models import Alumnos, Asignaturas, Asistencias, Citas, Notas, Profesor, Trabajos


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

    
def encuesta(request):
    perfil=buscar_alumno_dni(request)
    return render(request,'contenidoEncuesta.html',{"perfil":perfil})

def incidenciasAlumno(request):
    perfil=buscar_alumno_dni(request)
    inci=incidencias_al(request)
    return render(request,'contenidoIncidencias.html',{"incidencias":inci,"perfil":perfil})

def tutorCurso(request):
    tutor=buscar_tutor(request)
    perfil=buscar_alumno_dni(request)
    return render(request,'contenidoTutor.html',{"tutor":tutor,"perfil":perfil})

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
        
def buscar_profesor(my_frm):
    try:
        prof=Profesor.objects.get(nombre=my_frm.cleaned_data["profesor"])
    except Profesor.DoesNotExist:
            return None
    else:
        return prof
    
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
    
def incidencias_al(request):
     
    try:
        inci=Asistencias.objects.get_queryset().filter(dni_alumnos=request.session["logueado"]["dni"])
    except Notas.DoesNotExist:
            return None
    else:
        return inci
    
def anadirCita(request):
    perfil=buscar_alumno_dni(request)
    if request.method=='POST':
        my_frm=CitaForm(request.POST)
        if my_frm.is_valid():
            profesor=buscar_profesor(my_frm)
            if(profesor==None):
                return render(request,'contenidoCitas.html',{'form':my_frm,"perfil":perfil,"mensaje":"No existe ningún profesor con ese nombre"})
            timeNow = datetime.date.today()
            formatedTimeNow = timeNow.strftime("%Y-%m-%d")
            cita=Citas(profesor.dni,perfil.dni,formatedTimeNow,my_frm.cleaned_data["motivo"])
            cita.save()
            return redirect("base")
    else:
        my_frm=CitaForm()
    return render(request,'contenidoCitas.html',{'form':my_frm,"perfil":perfil})

