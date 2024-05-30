from django import forms

class Login(forms.Form):
    usuario=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"Tu usuario"}),label="Usuario")
    contrasena=forms.CharField(max_length=50,required=True,widget=forms.PasswordInput(attrs= {'class':'form-control','placeholder':"Tu contraseña"}),label="Contraseña")

class CitaForm(forms.Form):
    profesor=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"Nombre del profesor"}))
    motivo=forms.CharField(max_length=200,required=True,widget=forms.Textarea(attrs= {'class':'form-control','placeholder':"Motivo de la reunion"}),label="Nombre")