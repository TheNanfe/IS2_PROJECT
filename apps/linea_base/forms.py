from django import forms
from apps.linea_base.models import LineaBase

class LineaBaseForm(forms.ModelForm):
    class Meta:
        model = LineaBase
        fields = [
            'nombre',
            'id_proyecto',
            'estado'
        ]
        labels = {
            'nombre': 'Nombre de linea base',
            'id_proyecto': 'proyecto a asignar linea base',
            'estado': 'Estado de la linea base',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'id_proyecto': forms.Select(attrs={'class': 'form-control'}),
            'Estado': forms.Select(attrs={'class': 'form-control'}),
        }

