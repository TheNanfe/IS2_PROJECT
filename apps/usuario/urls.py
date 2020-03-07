from django.urls import path

from apps.usuario.views import RegistroForm, LoginView, LogoutView

urlpatterns = [
    path('registrar/', RegistroForm.as_view(), name="registrar"),
]
