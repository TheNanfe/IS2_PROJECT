from django.contrib.auth.models import User
from apps.rol.models import Rol
from django.contrib.auth.forms import UserCreationForm
from django import forms



class RegistroRol(forms.ModelForm):
    class Meta:
        model = Rol
        fields = [
            'nombre',
            'descripcion',

        ]
        labels = {
            'nombre': 'Nombre del Rol',
            'descripcion': 'descripcion del Rol',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }

