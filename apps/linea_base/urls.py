from django.urls import path
from apps.linea_base.views import *

urlpatterns = [
    path('listar_lineabase', listar_linea_base.as_view(), name='listar_lineabase'),
    path('editar_lineabase/<int:pk>', editar_linea_base.as_view(), name='editar_lineabase'),
    path('eliminar_lineabase/<int:pk>', eliminar_linea_base.as_view(), name= 'eliminar_lineabase'),
    path('crear_lineabase', crear_linea_base.as_view(), name='crear_lineabase'),
    path('tareas_lb/<int:pk>', BringTasks.as_view(), name='tareas_lb'),
    path('grafica-lineabase', linea_base_chart, name='grafica-lineabase'),
]
