from django.contrib.auth.models import User
from apps.usuario.models import UsuarioSistema
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegistroForm(UserCreationForm):
    class Meta:
        model = UsuarioSistema
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'Rol',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo',
            'Rol': 'Rol asignado',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'Rol': forms.Select(attrs={'class': 'form-control'}),
        }