from django.urls import path
from apps.usuario.views import RegistroForm, LoginView, LogoutView, RegistroNuevo
from apps.usuario.views import UsuarioList, editarUsuario, UsuarioDelete
from . import views

urlpatterns = [
    path('registrar/', RegistroForm.as_view(), name="registrar_usuario"),
    path('lista_usuario/', UsuarioList.as_view(), name="listar_usuario"),
    path('editar/<int:pk>', editarUsuario.as_view(), name="editar_usuario"),
    path('eliminar/<int:pk>/', UsuarioDelete.as_view(), name='eliminar_usuario'),
    path('registrar_nuevo/', RegistroNuevo.as_view(), name="registrar_usuario_nuevo"),
    
]
