from django import forms
from apps.proyecto.models import Proyecto
from apps.tarea.models import Tarea
'''choices = list(Tarea.objects.values_list('id', flat=True))
def converter(choices):
    lista = []
    for x in range (0, len(choices)):
        this = [str(choices[x]),str(choices[x])]
        lista.append(tuple(this))
    return tuple(lista)
z = converter(choices)'''


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = [
            'version',
            'prioridad',
            'estado',
            'descripcion',
            'observacion',
            'id_tarea_padre',
            'id_proyecto',
        ]
        labels = {
            'version': 'Version de la Tarea',
            'prioridad': 'Prioridad de la Tarea',
            'estado': 'En que estado se encuetra la tarea',
            'descripcion': 'Descripcion de la tarea',
            'observacion': 'Alguna observacion?',
            'id_tarea_padre': 'ID tarea padre',
            'id_proyecto': 'ID del proyecto al que pertenece',
        }
        widgets = {
            'version': forms.TextInput(attrs={'class': 'form-control'}),
            'prioridad': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'observacion': forms.TextInput(attrs={'class': 'form-control'}),
            'id_tarea_padre': forms.Select(attrs={'class': 'form-control'}),
            'id_proyecto': forms.Select(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('Tarea', None)
        super(TareaForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(TareaForm, self).clean()
        id_padre = cleaned_data.get('id_tarea_padre')
        id_proyecto = cleaned_data.get('id_proyecto')
        #variable = Tarea.objects.values_list('id', flat=True).filter(id_tarea_padre=str(id_padre))
        #proyectos = Proyecto.objects.values_list('id', flat=True).get(pk=str(id_proyecto))
        if id_padre != None:
            proyecto = Tarea.objects.values_list('id_proyecto', flat=True).get(pk=str(id_padre))
            print(proyecto)
            print(id_proyecto)
            if str(id_proyecto) == str(proyecto):
                print('felicidades!')
            else:
                raise forms.ValidationError(
                "Deben ser del mismo Proyecto"
            )

