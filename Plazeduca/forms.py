import datetime
from django import forms

class Login(forms.Form):
    usuario=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"Tu usuario"}),label="Usuario")
    contrasena=forms.CharField(max_length=50,required=True,widget=forms.PasswordInput(attrs= {'class':'form-control','placeholder':"Tu contraseña"}),label="Contraseña")

class CitaForm(forms.Form):
    receptor=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"Nombre con quien quieres la reunión"}))
    motivo=forms.CharField(max_length=200,required=True,widget=forms.Textarea(attrs= {'class':'form-control','placeholder':"Motivo de la reunion"}),label="Nombre")

class TrabajoForm(forms.Form):
    trabajo=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"Nombre del trabajo"}))
    fecha_inicial = forms.DateField(required=True,widget=forms.DateInput(attrs={'class': 'form-control','placeholder': 'Fecha de inicio','type': 'date'}))
    fecha_final = forms.DateField(required=True,widget=forms.DateInput(attrs={'class': 'form-control','placeholder': 'Fecha de inicio','type': 'date'}))
    receptor = forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombre del Alumno'}))
    nom_asignatura = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombre de la asignatura'}))


    def clean_fecha(self):
        fecha_inicial = self.cleaned_data["fecha_inicial"]
        fecha_final =self.cleaned_data["fecha_final"]

        if fecha_inicial and fecha_final:
            if fecha_inicial > fecha_final:
                raise forms.ValidationError("La fecha inicial no puede ser posterior a la fecha final")
        return fecha_inicial
    
    def clean_fecha_final(self):
        fecha_inicial = self.cleaned_data["fecha_inicial"]
        fecha_final =self.cleaned_data["fecha_final"]

        if fecha_inicial and fecha_final:
            if fecha_final < fecha_inicial:
                raise forms.ValidationError("La fecha final no puede ser anterior a la fecha inicial")
        return fecha_final

class BuscarIncidenciasForm(forms.Form):
    receptor=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"Busca las incidencias de alumno introducido"}))
    
class AsignaturaForm(forms.Form):
    examen=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"Nombre del examen"}))
    nom_asignatura = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombre de la asignatura'}))
    receptor = forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombre del alumno'}))
    fecha_subida = forms.DateField(required=True,widget=forms.DateInput(attrs={'class': 'form-control','placeholder': 'Fecha de subida ','type': 'date'}))
    nota = forms.IntegerField(required=True,max_value=10,min_value=0,widget=forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Nota del alumno'}))
    
    def clean_fecha(self):
        fecha_subida = self.cleaned_data["fecha_subida"]
        
        if fecha_subida:
            if fecha_subida > datetime.date.today().strftime("%Y-%m-%d"):
                raise forms.ValidationError("La fecha inicial no puede ser posterior a la fecha de hoy")
        return fecha_subida
    

class IncidenciaForm(forms.Form):
    receptor = forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombre del Alumno'}))
    nom_asignatura = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombre de la asignatura'}))
    falta = forms.BooleanField(required=True,widget=forms.RadioSelect(choices=((True, 'Falta'), (False, 'Retraso'))))
    