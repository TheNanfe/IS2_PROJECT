from apps.rol.models import Rol
from django import forms


class RegistroRol(forms.ModelForm):
    posible_choices = (
        ('user_cre', 'user_creation'),
        ('user_list', 'user_list'),
        ('user_edit', 'user_edit'),
        ('user_del', 'user_delete'),
        ('rol_cre', 'rol_creation'),
        ('rol_list', 'rol_list'),
        ('rol_edit', 'rol_edit'),
        ('rol_del', 'rol_delete'),
        ('proy_cre', 'project_creation'),
        ('proy_list', 'project_list'),
        ('proy_edit', 'project_edit'),
        ('proy_del', 'project_delete'),
        ('task_cre', 'task_creation'),
        ('task_list', 'task_list'),
        ('task_edit', 'task_edit'),
        ('task_del', 'tasl_delete'),
        ('lb_cre', 'lb_creation'),
        ('lb_list', 'lb_list'),
        ('lb_edit', 'lb_edit'),
        ('lb_del', 'lb_delete'),
    )
    
    class Meta:
       
        model = Rol
        fields = [
            'nombre',
            'descripcion',
            'choices',

        ]
        labels = {
            'nombre': 'Nombre del Rol',
            'descripcion': 'descripcion del Rol',
            'estado': 'Permisos del Rol',
            'choices': 'blabla',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'choices': forms.HiddenInput(),
        }
    Permisos = forms.MultipleChoiceField(choices=posible_choices, widget=forms.CheckboxSelectMultiple)
