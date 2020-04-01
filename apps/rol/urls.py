from django.urls import path
from apps.rol.views import RegistroRol, RolList, RolDelete, EditarRol
urlpatterns = [
    path('registrar/', RegistroRol.as_view(), name="registrar_rol"),
    path('listar/', RolList.as_view(), name="Listar"),
    path('editar/<int:pk>', EditarRol.as_view(), name="editar_rol"),
    path('eliminar/<int:pk>/',RolDelete.as_view(), name='eliminar_rol'),
]
