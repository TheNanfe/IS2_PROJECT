from django.urls import path, include
from apps.proyecto.views import index

urlpatterns = [
    path('index/', index, name='index'),
]
