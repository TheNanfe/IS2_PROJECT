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
        print('\n\n\n\n\n',id_padre,'\n\n\n\n\n')
        id_lb = str(cleaned_data.get('id_lineabase'))
        valor_padre = id_padre[len(id_proyecto)+3:]
        padres = Tarea.objects.all().values_list('id_tarea_padre', flat=True)
        print(valor_padre)
        if valor_padre != '' and valor_padre in str(padres):
            raise forms.ValidationError(
                "La tarea seleccionada ya es padre de otra, seleccione otra"
            )

        if id_padre != 'None':
            long = len(id_proyecto)
            if id_proyecto == id_lb[0:long] and id_proyecto == id_padre[0:long]:
                print('felicidades!')
            elif id_lb == '' or id_lb == 'None':
                raise forms.ValidationError(
                    "Para tener un padre deber pertenecer a alguna LB"
                )
            else:
                raise forms.ValidationError(
                "Deben ser del mismo Proyecto"
                )
            
            if id_lb != '' and id_lb != 'None':
                lb = Tarea.objects.get(pk=str(valor_padre))
                lb = str(lb.id_lineabase)
                print(id_lb[long+5:],lb[long+5:])
                if lb[long+5:] != id_lb[long+5:]:
                    raise forms.ValidationError(
                        "Las lineas bases difieren"
                    )

 