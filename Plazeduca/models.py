from django.db import models

class Alumnos(models.Model):
    usuario=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    dni=models.CharField(max_length=9,primary_key=True)
    nombre=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    telefono=models.CharField(max_length=50)
    fecha_nac=models.DateField()
    email=models.EmailField(max_length=50)
    dirreccion=models.CharField(max_length=50)
    cursos=models.CharField(max_length=20)
    faltas=models.IntegerField()
    retrasos=models.IntegerField()
    
    
class Profesor(models.Model):
    usuario=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    dni=models.CharField(max_length=9,primary_key=True)
    nombre=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    telefono=models.CharField(max_length=50)
    fecha_nac=models.DateField()
    email=models.EmailField(max_length=50)
    dirreccion=models.CharField(max_length=50)
    cursos=models.CharField(max_length=20)
    tutoria=models.CharField(max_length=50)
    

class Administrador(models.Model):
    usuario=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    
class Cursos(models.Model):
    nombre=models.CharField(max_length=50)
    siglas=models.CharField(max_length=20,primary_key=True)
    
class Asginaturas(models.Model):
    nombre=models.CharField(max_length=50,primary_key=True)
    horas_semanales=models.IntegerField()
    dni_alumnos=models.CharField(max_length=9)
    dni_profesor=models.CharField(max_length=9)
    curso=models.CharField(max_length=20)
    
class Notas(models.Model):
    nota=models.IntegerField()
    dni_alumno=models.CharField(max_length=9,primary_key=True)
    nom_asignatura=models.CharField(max_length=50)
    
class Asistencias(models.Model):
    dni_alumnos=models.CharField(max_length=9,primary_key=True)
    num_faltas=models.IntegerField()
    num_retrasos=models.IntegerField()
    nom_asignatura=models.CharField(max_length=50)
    
class Trabajos(models.Model):
    trabajo=models.CharField(max_length=50)
    fecha_inicio=models.DateField()
    fecha_entrega=models.DateField()
    dni_alumnos=models.CharField(max_length=9,primary_key=True)
    nom_asignatura=models.CharField(max_length=50)
    
class Citas(models.Model):
    dni_profesor=models.CharField(max_length=50)
    dni_alumnos=models.CharField(max_length=20,primary_key=True)
    fecha_envio=models.DateField()
    motivo=models.TextField(max_length=100)
    

    
    