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

<<<<<<< Updated upstream
from Plazeduca.views import inicio,base,cerrarS,ver_perfil
=======
from Plazeduca.views import inicio,base,cerrarS,tutor, ver_notas
>>>>>>> Stashed changes
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio,name="login"),
    path('base',base,name="base"),
    path('cerrarSesion',cerrarS,name="cerrar"),
<<<<<<< Updated upstream
    path('perfil',ver_perfil,name="perfil")
=======
    path('tutor',tutor,name="perfilTutor"),
    path('notas',ver_notas,name="notas")
>>>>>>> Stashed changes
]
