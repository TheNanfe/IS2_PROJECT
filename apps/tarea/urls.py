from django.urls import path
from apps.tarea.views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('listar_tarea', listar_tarea.as_view(), name='listar_tarea'),
    path('editar_tarea/<int:pk>', editar_tarea.as_view(), name='editar_tarea'),
    path('eliminar_tarea/<int:pk>', eliminar_tarea.as_view(), name='eliminar_tarea'),
    path('crear_tarea', crear_tarea.as_view(), name='crear_tarea'),
    path('listar_lineabase', listar_linea_base.as_view(), name='listar_lineabase'),
    path('editar_lineabase/<int:pk>', editar_linea_base.as_view(), name='editar_lineabase'),
    path('eliminar_lineabase/<int:pk>', eliminar_linea_base.as_view(), name= 'eliminar_lineabase'),
    path('crear_lineabase', crear_linea_base.as_view(), name='crear_lineabase'),
]
