from django import forms
from apps.linea_base.models import LineaBase
'''choices = list(Tarea.objects.values_list('id', flat=True))
def converter(choices):
    lista = []
    for x in range (0, len(choices)):
        this = [str(choices[x]),str(choices[x])]
        lista.append(tuple(this))
    return tuple(lista)
z = converter(choices)'''


class LineaBaseForm(forms.ModelForm):
    class Meta:
        model = LineaBase
        fields = [
            'nombre',
            'id_tarea',
        ]
        labels = {
            'nombre': 'Nombre de linea base',
            'id_tarea': 'Tareas a asignar linea base',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'id_tarea': forms.CheckboxSelectMultiple(),
        }

