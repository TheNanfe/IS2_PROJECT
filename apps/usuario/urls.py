from django.urls import path

from apps.usuario.views import RegistroForm, LoginView, LogoutView
from apps.usuario.views import UsuarioList, editarUsuario, UsuarioDelete

urlpatterns = [
    path('registrar/', RegistroForm.as_view(), name="registrar"),
    path('lista_usuario/', UsuarioList.as_view(), name="lista_usuario"),
    path('editar/<int:pk>', editarUsuario.as_view(), name="editar_usuario"),
    path('eliminar/<int:pk>/', UsuarioDelete.as_view(), name='eliminar_usuario'),
]
