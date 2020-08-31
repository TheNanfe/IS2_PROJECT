from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput
from django import forms
from apps.proyecto.models import Proyecto


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = [
            'nombre',
            'codigo',
            'fecha_inicio',
            'fecha_fin',
            'estado',
            'sprint',
            'tarea',
            'cliente',
        ]
        labels = {
            'nombre': 'Nombre del proyecto',
            'codigo': 'Codigo del proyecto',
            'fecha_inicio': 'Fecha de inicio del proyecto',
            'fecha_fin': 'Fecha fin estimada del proyecto',
            'estado': 'Estado del proyecto',
            'sprint': 'Duracion de sprints',
            'tarea': 'Tareas a hacer',
            'cliente': 'Cliente',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio': DatePickerInput(format='%Y-%m-%d'),
            'fecha_fin': DatePickerInput(format='%Y-%m-%d'),
            'fecha_inicio': DatePickerInput(),
            'fecha_fin': DatePickerInput(),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'sprint': forms.TextInput(attrs={'class': 'form-control'}),
            #'tarea': forms.TextInput(attrs={'class': 'form-control'}),
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'tarea':forms.Select(attrs={'class': 'form-control'}),
        }
