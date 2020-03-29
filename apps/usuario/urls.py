from django.urls import path

from apps.usuario.views import RegistroForm, LoginView, LogoutView
from apps.proyecto.views import UsuarioList

urlpatterns = [
    path('registrar/', RegistroForm.as_view(), name="registrar"),
]
