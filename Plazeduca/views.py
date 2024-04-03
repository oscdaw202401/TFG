from django.shortcuts import redirect, render
from Plazeduca.forms import Login
from Plazeduca.models import Alumnos, Notas


def inicio(request):
    if request.method=='POST':
        my_frm=Login(request.POST)
        if my_frm.is_valid():
            alum=buscar_alumno(my_frm)
            request.session['logueado']={"dni":alum.dni}
            return redirect('home')
    else:
        my_frm=Login()
    return render(request,'login.html',{'form':my_frm})
    
def home(request):
    return render(request,'contenido.html')

def buscar_alumno(my_frm):
    try:
        alum=Alumnos.objects.get(usuario=my_frm.cleaned_data["usuario"],password=my_frm.cleaned_data["contrasena"])
    except Alumnos.DoesNotExist:
            return None
    else:
        return alum
    
def notas_al(request):
    try:
        notas=Notas.objects.get(dni_alumno=request.session["logueado"])
    except Alumnos.DoesNotExist:
            return None
    else:
        return notas