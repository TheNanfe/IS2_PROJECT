from apps.rol.models import Rol
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
