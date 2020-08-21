from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput
from django import forms
from apps.tarea.models import Tarea
from django.forms.widgets import Select


class TareaForm(forms.ModelForm):
    class Meta:
        #CHOICES  = Tarea.objects.values_list('id', flat = True)
        model = Tarea
        fields = [
            'version',
            'prioridad',
            'estado',
            'descripcion',
            'observacion',
            'id_tarea_padre',
        ]
        labels = {
            'version': 'Version de la Tarea',
            'prioridad': 'Prioridad de la Tarea',
            'estado': 'En que estado se encuetra la tarea',
            'descripcion': 'Descripcion de la tarea',
            'observacion': 'Alguna observacion?',
            'id_tarea_padre': 'ID tarea padre',
        }
        print('hasta aca todo biben')
        widgets = {
            'version': forms.TextInput(attrs={'class': 'form-control'}),
            'prioridad': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'descripcion':forms.TextInput(attrs={'class': 'form-control'}),
            'observacion': forms.TextInput(attrs={'class': 'form-control'}),
            #'id_tarea_padre':Select(choices=((x) for x in CHOICES)),
            #'id_tarea_padre': forms.Select(attrs={'class': 'form-control'}),
            'id_tarea_padre': forms.TextInput(attrs={'class': 'form-control'}),

        }
