from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render
from Plazeduca.forms import Login
from Plazeduca.models import Alumnos, Notas, Trabajos


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
    notas=notas_al(request)
    trabajos=trabajos_al(request)
    return render(request,'contenidoAlumno.html',{"sesion":request.session["logueado"]["dni"],"notas":notas,"trabajos":trabajos})


def cerrarS(request):
    logout(request)
    return redirect('login')

def buscar_alumno(my_frm):
    try:
        alum=Alumnos.objects.get(usuario=my_frm.cleaned_data["usuario"],password=my_frm.cleaned_data["contrasena"])
    except Alumnos.DoesNotExist:
            return None
    else:
        return alum
    
def buscar_alumno(request):
    try:
        alum=Alumnos.objects.get(dni=request.session["logueado"]["dni"])
    except Alumnos.DoesNotExist:
            return None
    else:
        return alum
    
def notas_al(request):
    try:
        notas=Notas.objects.all()
    except Notas.DoesNotExist:
            return None
    else:
        return notas
    
def trabajos_al(request):
    
    try:
        notas=Trabajos.objects.all()
    except Notas.DoesNotExist:
            return None
    else:
        return notas
    
