from django.db import models
from apps.proyecto.models import Proyecto
#from apps.tarea.models import Tarea


class LineaBase(models.Model):
    nombre = models.CharField(max_length=50)
    id_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=True, blank=True) 
    #tareas = models.CharField(max_length=50)
    choices = (
        ('A', 'ACTIVO' ),
        ('I', 'INNACTIVO'),
    )
    estado = models.CharField(max_length=10, choices=choices,null=False, blank=False)

    def __str__(self):
        return str(self.id_proyecto)+': LB-'+str(self.nombre)
