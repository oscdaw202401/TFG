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
            prof=buscar_profesor(my_frm)
            if(alum!=None):
                request.session['logueado']={"dni":alum.dni}
                return redirect('base')
            elif(prof!=None):
                request.session['logueado']={"dni":prof.dni}
                return redirect('base')
            else:
                return render(request,'login.html',{'form':my_frm,'mensaje':"Nombre de usuario o contraseña incorrecto"})
    else:
        my_frm=Login()
    return render(request,'login.html',{'form':my_frm})
    
def base(request):
    perfil=buscar_alumno_dni(request)
    if(perfil==None):
        perfil=buscar_profesor_dni(request)
        return render(request,'contenidoProfesor.html',{"sesion":request.session["logueado"]["dni"],"perfil":perfil})
    return render(request,'contenidoAlumno.html',{"sesion":request.session["logueado"]["dni"],"perfil":perfil})

#Alumnos

def notasAlumno(request):
    notas=notas_al(request)
    perfil=buscar_alumno_dni(request)
    return render(request,'contenidoNotas.html',{"sesion":request.session["logueado"]["dni"],"notasAlumno":notas,"perfil":perfil,"rol":"alumno"})

def trabajosAlumno(request):
    trabajos=trabajos_al(request)
    perfil=buscar_alumno_dni(request)
    return render(request,'contenidoTrabajos.html',{"sesion":request.session["logueado"]["dni"],"trabajos":trabajos,"perfil":perfil,"rol":"alumno"})

def asignaturas(request):
    asig=buscar_asignaturas_alumno(request)
    perfil=buscar_alumno_dni(request)
    return render(request,'contenidoAsignaturas.html',{"asig":asig,"perfil":perfil,"rol":"alumno"})

def encuesta(request):
    perfil=buscar_alumno_dni(request)
    rol="alumno"
    if(perfil==None):
        perfil=buscar_profesor_dni(request)
        rol="profesor"
    return render(request,'contenidoEncuesta.html',{"perfil":perfil,"rol":rol})

def incidenciasAlumno(request):
    perfil=buscar_alumno_dni(request)
    inci=incidencias_al(request)
    return render(request,'contenidoIncidencias.html',{"incidencias":inci,"perfil":perfil,"rol":"alumno"})

def tutorCurso(request):
    tutor=buscar_tutor(request)
    perfil=buscar_alumno_dni(request)
    return render(request,'contenidoTutor.html',{"tutor":tutor,"perfil":perfil,"rol":"alumno"})



        

#Profesor

def trabajosProfesor(request):
    prof=buscar_profesor_dni(request)
    trab=buscar_trabajos_asignatura_profesor(request)
    return render(request,'contenidoTrabajos.html',{"trabajos":trab,"perfil":prof,"rol":"profesor"})

def asignaturasProfesor(request):
    prof=buscar_profesor_dni(request)
    asig=buscar_asignatura_profesor(request)
    return render(request,'contenidoAsignaturas.html',{"asig":asig,"perfil":prof,"rol":"profesor"})

def notasProfesor(request):
    prof=buscar_profesor_dni(request)
    asig=buscar_asignatura_profesor(request)
    return render(request,'contenidoAsignaturas.html',{"asig":asig,"perfil":prof,"rol":"profesor"})




#Busquedas

def buscar_alumno(my_frm):
    try:
        alum=Alumnos.objects.get(usuario=my_frm.cleaned_data["usuario"],password=my_frm.cleaned_data["contrasena"])
    except Alumnos.DoesNotExist:
            return None
    else:
        return alum
    

def buscar_profesor(my_frm):
    try:
        prof=Profesor.objects.get(usuario=my_frm.cleaned_data["usuario"],password=my_frm.cleaned_data["contrasena"])
    except Profesor.DoesNotExist:
            return None
    else:
        return prof
    
def buscar_alumno_dni(request):
    try:
        alum=Alumnos.objects.get(dni=request.session["logueado"]["dni"])
    except Alumnos.DoesNotExist:
            return None
    else:
        return alum
    
def buscar_profesor_nombre(my_frm):
    try:
        prof=Profesor.objects.get(nombre=my_frm.cleaned_data["profesor"])
    except Profesor.DoesNotExist:
            return None
    else:
        return prof
    
def buscar_profesor_dni(request):
    try:
        prof=Profesor.objects.get(dni=request.session["logueado"]["dni"])
    except Profesor.DoesNotExist:
            return None
    else:
        return prof

def buscar_tutor(request):
    try:
        alum=buscar_alumno_dni(request)
        tutor=Profesor.objects.get(tutoria=alum.cursos)
    except Profesor.DoesNotExist:
            return None
    else:
        return tutor
        
def buscar_asignaturas_alumno(request):
    alum=buscar_alumno_dni(request)
    try:
        asig=Asignaturas.objects.get_queryset().filter(curso=alum.cursos)
    except Asignaturas.DoesNotExist:
        return None
    else:
        return asig
    
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
    

def buscar_trabajos_asignatura_profesor(request):
    try:
        asig=buscar_asignatura_profesor(request)
        listaTrabajos=[]
        for a in asig:
            trab=Trabajos.objects.get_queryset().filter(nom_asignatura=a.nombre)
            listaTrabajos.extend(trab)
    except Trabajos.DoesNotExist or listaTrabajos.count==0:
            return None
    else:
        return listaTrabajos


def buscar_asignatura_profesor(request):
    try:
        prof=buscar_profesor_dni(request)
        asig=Asignaturas.objects.get_queryset().filter(profesor=prof.nombre)
    except Asignaturas.DoesNotExist:
            return None
    else:
        return asig

def cerrarS(request):
    logout(request)
    return redirect('login')

def anadirCita(request):
    perfil=buscar_alumno_dni(request)
    if request.method=='POST':
        my_frm=CitaForm(request.POST)
        if my_frm.is_valid():
            profesor=buscar_profesor_nombre(my_frm)
            if(profesor==None):
                return render(request,'contenidoCitas.html',{'form':my_frm,"perfil":perfil,"mensaje":"No existe ningún profesor con ese nombre"})
            timeNow = datetime.datetime.now()
            lastId=Citas.objects.latest("id").id+1
            formatedTimeNow = timeNow.strftime("%Y-%m-%d %H:%M:%S")
            cita=Citas(lastId,profesor.dni,perfil.dni,formatedTimeNow,my_frm.cleaned_data["motivo"])
            cita.save()
            return redirect("base")
    else:
        my_frm=CitaForm()
    return render(request,'contenidoCitas.html',{'form':my_frm,"perfil":perfil})

