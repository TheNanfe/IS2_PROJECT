from django.db import models
from apps.proyecto.models import Proyecto

class Tarea(models.Model):
    version = models.CharField(max_length=50)
    prioridad_tarea = (
        ('Alta', 'Alta'),
        ('Med', 'Media'),
        ('Baja', 'Baja'),
    )
    prioridad = models.CharField(max_length=10, choices=prioridad_tarea)
    estado_tarea = (
        ('PEN', 'PENDIENTE'),
        ('FIN', 'FINALIZADO'),
        ('INI', 'INICIADO'),
    )
    estado = models.CharField(max_length=3, choices=estado_tarea)
    descripcion = models.CharField(max_length=50)
    observacion = models.CharField(max_length=50, null=True, blank=True)
    id_tarea_padre = models.ForeignKey('Tarea', on_delete=models.CASCADE, null=True, blank=True)
    id_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.id)



