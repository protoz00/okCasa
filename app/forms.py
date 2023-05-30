from pyexpat import model
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class FormularioUserRegistro(UserCreationForm):
	class Meta:
            model = User
            fields = ['username','first_name','last_name','email','password1','password2']

class SolicitudForm(forms.ModelForm):
     class Meta:
          model = Solicitud
          fields = '__all__'
          exclude = ['run_emp','id_solicitud']

          
