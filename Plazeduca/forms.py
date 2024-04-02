from django import forms

class Login(forms.Form):
    usuario=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"Tu usuario"}),label="Usuario")
    contrasena=forms.CharField(max_length=50,required=True,widget=forms.PasswordInput(attrs= {'class':'form-control','placeholder':"Tu contraseña"}),label="Contraseña")