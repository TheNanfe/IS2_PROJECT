from django.urls import path
from apps.rol.views import RegistroRol, RolList, RolDelete, EditarRol, BringUsuarios
urlpatterns = [
    path('registrar/', RegistroRol.as_view(), name="registrar_rol"),
    path('listar/', RolList.as_view(), name="listar_rol"),
    path('editar/<int:pk>', EditarRol.as_view(), name="editar_rol"),
    path('eliminar/<int:pk>/',RolDelete.as_view(), name='eliminar_rol'),
    path('listar_usuarios/<int:pk>',BringUsuarios.as_view(), name='listar_usuarios')
]
