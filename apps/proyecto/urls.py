from django.urls import path, include
from apps.proyecto.views import index, proyecto_list,  proyecto_create, proyecto_delete, proyecto_edit

urlpatterns = [
    path('index/', index, name='index'),
    path('proyecto_list', proyecto_list.as_view(), name='listar_proyecto'),
    path('proyecto_edit/<int:pk>', proyecto_edit.as_view(), name='editar_proyecto'),
    path('proyecto_delete/<int:pk>', proyecto_delete.as_view(), name='eliminar_proyecto'),
    path('proyecto_create', proyecto_create.as_view(), name='crear_proyecto'),
]
