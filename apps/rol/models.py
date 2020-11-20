from django.db import models
from django.contrib.postgres.fields import ArrayField

class Rol(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=100, null=True)
    posible_choices = (
        ('user_cre', 'user_creation'),
        ('user_list', 'user_list'),
        ('user_del', 'user_delete'),
        ('user_edit', 'user_edit'),
        ('rol_cre', 'rol_creation'),
        ('rol_list', 'rol_creation'),
        ('rol_edit', 'rol_edit'),
        ('rol_del', 'rol_delete'),
        ('proy_cre', 'project_creation'),
        ('proy_list', 'project_creation'),
        ('proy_edit', 'project_edit'),
        ('proy_del', 'project_delete'),
        ('task_cre', 'task_creation'),
        ('task_list', 'task_creation'),
        ('task_edit', 'task_edit'),
        ('task_del', 'tasl_delete'),
        ('lb_cre', 'lb_creation'),
        ('lb_list', 'lb_creation'),
        ('lb_edit', 'lb_edit'),
        ('lb_del', 'lb_delete'),
    )
    '''choices = ArrayField(
        models.CharField(choices=posible_choices, max_length=30, blank=True, default='none'),
    )'''
    
    
    @classmethod
    def get_id(self):
        return self.id
    
    def __str__(self):
       return '{}'.format(self.nombre)
