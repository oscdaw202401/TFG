import datetime
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from Plazeduca.forms import BuscarIncidenciasForm, CitaForm, Login, TrabajoForm
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
        return render(request,'contenidoProfesor.html',{"sesion":request.session["logueado"]["dni"],"perfil":perfil,"rol":"profesor"})
    return render(request,'contenidoAlumno.html',{"sesion":request.session["logueado"]["dni"],"perfil":perfil,"rol":"alumno"})

#Alumnos

def notasAlumno(request):
    notas=buscar_notas_al(request)
    perfil=buscar_alumno_dni(request)
    return render(request,'contenidoNotas.html',{"sesion":request.session["logueado"]["dni"],"notas":notas,"perfil":perfil,"rol":"alumno"})

def trabajosAlumno(request):
    trabajos=buscar_trabajos_al(request)
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
    inci=buscar_incidencias_al(request)
    return render(request,'contenidoIncidencias.html',{"incidencias":inci,"perfil":perfil,"rol":"alumno"})

def tutorCurso(request):
    tutor=buscar_tutor(request)
    perfil=buscar_alumno_dni(request)
    return render(request,'contenidoTutor.html',{"tutor":tutor,"perfil":perfil,"rol":"alumno"})

def mostrarCalendario(request):
    perfil=buscar_alumno_dni(request)
    rol="alumno"
    if(perfil==None):
        perfil=buscar_profesor_dni(request)
        rol="profesor"
    return render(request,'contenidoCalendario.html',{"perfil":perfil,"rol":rol})

        

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
    notas=buscar_nota_asignatura_alumno(request)
    return render(request,'contenidoNotas.html',{"notas":notas,"perfil":prof,"rol":"profesor"})

def tutoriaClase(request):
    prof=buscar_profesor_dni(request)
    alum=buscar_alumnos_tutoria(request)
    return render(request,'contenidoTutor.html',{"alum":alum,"perfil":prof,"rol":"profesor"})

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
    
def buscar_alumno_dni_Nsession(alum):
    try:
        alum=Alumnos.objects.get(dni=alum.dni_alumno)
    except Alumnos.DoesNotExist:
            return None
    else:
        return alum
    
def buscar_profesor_nombre_apellidos(my_frm):
    nombreYapellidos=my_frm.cleaned_data["nombre_alumno"].split()
    try:
        prof=Profesor.objects.get(nombre=nombreYapellidos[0],apellidos=" ".join(nombreYapellidos[1:]))
    except Profesor.DoesNotExist:
            return None
    else:
        return prof
    
def buscar_alumno_nombre_apellidos(my_frm):
    nombreYapellidos=my_frm.cleaned_data["nombre_alumno"].split()
    try:
        alum=Alumnos.objects.get(nombre=nombreYapellidos[0],apellidos=" ".join(nombreYapellidos[1:]))
    except Alumnos.DoesNotExist:
            return None
    else:
        return alum
    
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
    
def buscar_notas_al(request):
    try:
        notas=Notas.objects.get_queryset().filter(dni_alumno=request.session["logueado"]["dni"])
    except Notas.DoesNotExist:
            return None
    else:
        return notas
    
def buscar_trabajos_al(request):
    try:
        notas=Trabajos.objects.get_queryset().filter(dni_alumnos=request.session["logueado"]["dni"])
    except Trabajos.DoesNotExist:
            return None
    else:
        return notas
    
def buscar_incidencias_al(request):
    try:
        inci=Asistencias.objects.get_queryset().filter(dni_alumnos=request.session["logueado"]["dni"])
    except Asistencias.DoesNotExist:
            return None
    else:
        return inci
    
def buscar_incidencias_dni(al):
    try:
        dicIncidencias={}
        inci=Asistencias.objects.get_queryset().filter(dni_alumnos=al.dni)
        name=f"{al.nombre} {al.apellidos}"
        if (inci!=None):
            dicIncidencias[name]=inci
    except Asistencias.DoesNotExist:
            return None
    else:
        return dicIncidencias
    
def buscar_incidencias_todos(request):
    try:
        alumnosCurso=buscar_alumnos_tutoria(request)
        dicIncidencias={}
        for al in alumnosCurso:
            name=f"{al.nombre} {al.apellidos}"
            inci=Asistencias.objects.get_queryset().filter(dni_alumnos=al.dni)
            if inci.exists():
                dicIncidencias[name]=list(inci)
    except Asistencias.DoesNotExist:
            return None
    else:
        return dicIncidencias
    

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
    

def buscar_nota_asignatura_alumno(request):
    try:
        asig=buscar_asignatura_profesor(request)
        listNotas=[]
        for a in asig:
            nota=Notas.objects.get_queryset().filter(nom_asignatura=a.nombre)
            listNotas.extend(nota)
    except Notas.DoesNotExist:
            return None
    else:
        return listNotas
    
# def buscar_alumnos_por_nota(notas):
#     try:
#         listaAlumnos=[]
#         for n in notas:
#             alum=Alumnos.objects.get_queryset().filter(dni=n.dni_alumno)
#             listaAlumnos.extend(alum)
#     except Alumnos.DoesNotExist or listaAlumnos.count==0:
#             return None
#     else:
#         return listaAlumnos
    
def buscar_alumnos_tutoria(request):
    try:
        prof=buscar_profesor_dni(request)
        alum=Alumnos.objects.get_queryset().filter(cursos=prof.tutoria)
    except Alumnos.DoesNotExist:
            return None
    else:
        return alum

def cerrarS(request):
    logout(request)
    return redirect('login')

def anadir_cita(request):
    perfil=buscar_alumno_dni(request)
    rol="alumno"
    if(perfil==None):
        perfil=buscar_profesor_dni(request)
        rol="profesor"
    if request.method=='POST':
        my_frm=CitaForm(request.POST)
        if my_frm.is_valid():
            if(rol=="profesor"):
                reunion=buscar_alumno_nombre_apellidos(my_frm)
            reunion=buscar_profesor_nombre_apellidos(my_frm)
            if(reunion==None):
                return render(request,'contenidoCitas.html',{'form':my_frm,"perfil":perfil,"mensaje":"No existe nadie con ese nombre","rol":rol})
            timeNow = datetime.datetime.now()
            lastId=Citas.objects.latest("id").id+1
            formatedTimeNow = timeNow.strftime("%Y-%m-%d %H:%M:%S")
            cita=Citas(lastId,reunion.dni,perfil.dni,formatedTimeNow,my_frm.cleaned_data["motivo"])
            cita.save()
            return redirect("base")
    else:
        my_frm=CitaForm()
    return render(request,'contenidoCitas.html',{'form':my_frm,"perfil":perfil,"rol":rol})

def anadir_trabajo_profesor(request):
    perfil=buscar_profesor_dni(request)
    rol="profesor"
    if request.method=='POST':
        my_frm=TrabajoForm(request.POST)
        if my_frm.is_valid():
            alumno=buscar_alumno_nombre_apellidos(my_frm)
            if(alumno==None):
                return render(request,'anadirTrabajo.html',{'form':my_frm,"perfil":perfil,"mensaje":"El alumno introducido es incorrecto","rol":rol})
            trab=Trabajos(my_frm.cleaned_data["trabajo"],my_frm.clean_fecha(),my_frm.clean_fecha_final(),alumno.dni,my_frm.cleaned_data["nom_asignatura"])
            trab.save()
            return redirect("base")
    else:
        my_frm=TrabajoForm()
    return render(request,'anadirTrabajo.html',{'form':my_frm,"perfil":perfil,"rol":rol})

def incidencias_alumnos(request):
    perfil=buscar_profesor_dni(request)
    rol="profesor"
    if request.method=='POST':
        my_frm=BuscarIncidenciasForm(request.POST)
        if my_frm.is_valid():
            alumno=buscar_alumno_nombre_apellidos(my_frm)
            if(alumno==None):
                return render(request,'anadirTrabajo.html',{'form':my_frm,"perfil":perfil,"mensaje":"El alumno introducido es incorrecto","rol":rol})
            inci=buscar_incidencias_dni(alumno)
            my_frm=BuscarIncidenciasForm()
            return render(request,'contenidoIncidenciasAlumnos.html',{'form':my_frm,"perfil":perfil,"incidencias":inci,"rol":rol})
    else:
        my_frm=BuscarIncidenciasForm()
        inci=buscar_incidencias_todos(request)
    return render(request,'contenidoIncidenciasAlumnos.html',{'form':my_frm,"perfil":perfil,"incidencias":inci,"rol":rol})