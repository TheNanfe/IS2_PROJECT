from django import forms
from apps.proyecto.models import Proyecto
from apps.tarea.models import Tarea
from apps.linea_base.models import LineaBase


class TareaForm(forms.ModelForm):

    class Meta:
        model = Tarea
        fields = [
            'version',
            'prioridad',
            'estado',
            'descripcion',
            'observacion',
            'id_proyecto',
            'id_lineabase',
            'id_tarea_padre',
            
        ]
        labels = {
            'version': 'Version de la Tarea',
            'prioridad': 'Prioridad de la Tarea',
            'estado': 'En que estado se encuetra la tarea',
            'descripcion': 'Descripcion de la tarea',
            'observacion': 'Alguna observacion?',
            'id_proyecto': 'ID del proyecto al que pertenece',
            'id_lineabase': 'ID de la LB a la cual pertenecce',
            'id_tarea_padre': 'ID tarea padre',
            
        }
        widgets = {
            'version': forms.TextInput(attrs={'class': 'form-control'}),
            'prioridad': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'observacion': forms.TextInput(attrs={'class': 'form-control'}),
            'id_proyecto': forms.Select(attrs={'class': 'form-control'}),
            'id_tarea_padre': forms.Select(attrs={'class': 'form-control'}),
            'id_lineabase': forms.Select(attrs={'class': 'form-control'}),
        }
    #Permisos = forms.MultipleChoiceField(choices=choice, widget=forms.CheckboxSelectMultiple)
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('Tarea', None)
        super(TareaForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(TareaForm, self).clean()
        id_padre = str(cleaned_data.get('id_tarea_padre'))
        id_proyecto = str(cleaned_data.get('id_proyecto'))
        id_lb = str(cleaned_data.get('id_lineabase'))
        
        if id_padre != 'None':
            long = len(id_proyecto)
            print(id_padre[0:long], id_proyecto, id_lb[0:long])
            if id_proyecto == id_lb[0:long] and id_proyecto == id_padre[0:long]:
                print('felicidades!')
            else:
                raise forms.ValidationError(
                "Deben ser del mismo Proyecto"
            )

