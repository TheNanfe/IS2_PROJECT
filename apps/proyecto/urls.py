from django.urls import path, include
from apps.proyecto.views import index, UsuarioList

urlpatterns = [
    path('index/', index, name='index'),
    path('lista_usuario/', UsuarioList.as_view(), name="lista_usuario"),
]
