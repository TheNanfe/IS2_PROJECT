from django.urls import path

from apps.usuario.views import RegistroForm, LoginView, LogoutView
from apps.usuario.views import UsuarioList

urlpatterns = [
    path('registrar/', RegistroForm.as_view(), name="registrar"),
    path('lista_usuario/', UsuarioList.as_view(), name="lista_usuario"),
]
