from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from apps.proyecto.models import Proyecto
from apps.proyecto.forms import ProyectoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from apps.rol.models import Rol
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from apps.tarea.models import Tarea

PERMISO_CREATE = 'proy_cre'
PERMISO_LIST = 'proy_list'
PERMISO_EDIT = 'proy_edit'
PERMISO_DELETE = 'proy_del'


@login_required
def index(request):
    return render(request, 'proyecto/index.html')


class proyecto_list(LoginRequiredMixin, ListView):
    model = Proyecto
    template_name = 'proyecto/lista_proyectos.html'
    context_object_name = 'proyecto_list'
    paginate_by = 10
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            def controlador(request):
                try:
                    user_rol = Rol.objects.values_list('choices', flat=True).get(pk=str(request.user.rol.get_id()))
                except:
                    raise PermissionDenied("No tiene los permisos adecuados")
                if (PERMISO_LIST in user_rol or PERMISO_EDIT in user_rol or 
                PERMISO_DELETE in user_rol or request.user.is_superuser):
                    print('felicidades')
                    return 0
                else:
                    print(request.user.rol)
                    return 1
            if controlador(request) == 1:
                return HttpResponseRedirect(reverse_lazy('index'))
        return super(proyecto_list, self).dispatch(request,*args,**kwargs)


class proyecto_create(LoginRequiredMixin, CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'proyecto/proyecto_form.html'
    success_url = reverse_lazy('listar_proyecto')
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            def controlador(request):
                try:
                   user_rol = Rol.objects.values_list('choices', flat=True).get(pk=str(request.user.rol.get_id()))
                except:
                    raise PermissionDenied("Los passwords no coinciden")
                if PERMISO_CREATE in user_rol:
                    print('felicidades')
                    return 0
                else:
                    print(request.user.rol)
                    return 1
            if controlador(request) == 1:
                return HttpResponseRedirect(reverse_lazy('index'))
        return super(proyecto_create, self).dispatch(request,*args,**kwargs)


class proyecto_delete(LoginRequiredMixin, DeleteView):
    model = Proyecto
    template_name = 'proyecto/proyecto_delete.html'
    success_url = reverse_lazy('listar_proyecto')
    context_object_name = 'proyecto_delete'
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            def controlador(request):
                try:
                   user_rol = Rol.objects.values_list('choices', flat=True).get(pk=str(request.user.rol.get_id()))
                except:
                    raise PermissionDenied("Los passwords no coinciden")
                if PERMISO_CREATE in user_rol:
                    print('felicidades')
                    return 0
                else:
                    print(request.user.rol)
                    return 1
            if controlador(request) == 1:
                return HttpResponseRedirect(reverse_lazy('index'))
        return super(proyecto_delete, self).dispatch(request,*args,**kwargs)


class proyecto_edit(LoginRequiredMixin, UpdateView):
    model = Proyecto
    fields = ['nombre', 'codigo', 'fecha_inicio', 'fecha_fin', 'estado', 'sprint', 'cliente']
    template_name = 'proyecto/proyecto_form.html'
    success_url = reverse_lazy('listar_proyecto')
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            def controlador(request):
                try:
                   user_rol = Rol.objects.values_list('choices', flat=True).get(pk=str(request.user.rol.get_id()))
                except:
                    raise PermissionDenied("Los passwords no coinciden")
                if PERMISO_CREATE in user_rol:
                    print('felicidades')
                    return 0
                else:
                    print(request.user.rol)
                    return 1
            if controlador(request) == 1:
                return HttpResponseRedirect(reverse_lazy('index'))
        return super(proyecto_edit, self).dispatch(request,*args,**kwargs)


class BringTasks(ListView):
    template_name = 'tarea/lista_tareas.html'
    paginate_by = 10
    model = Tarea
    context_object_name = 'listar_tarea'
    queryset = Tarea.objects.all()#Tarea.objects.filter(id_lineabase=1)


    def get_queryset(self):
        valor = str(self.request)
        indice = valor[43:-2]
        print('\n\n\n\n',indice)
        queryset = Tarea.objects.all().filter(id_proyecto=indice)
        return queryset
