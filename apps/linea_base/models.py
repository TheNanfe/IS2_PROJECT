from django.db import models
from apps.proyecto.models import Proyecto
#from apps.tarea.models import Tarea


class LineaBase(models.Model):
    nombre = models.CharField(max_length=50)
    #id_tarea = models.ManyToManyField(Tarea, blank=True, null=True)
    id_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=True, blank=True) 
    tareas = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id_proyecto)+': LB-'+str(self.nombre)
