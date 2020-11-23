from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from apps.tarea.models import Tarea
from apps.tarea.forms import TareaForm
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.linea_base.models import LineaBase
from django.core.exceptions import PermissionDenied
from apps.rol.models import Rol
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

PERMISO_CREATE = 'task_cre'
PERMISO_LIST = 'task_list'
PERMISO_EDIT = 'task_edit'
PERMISO_DELETE = 'task_del'


@login_required
def index(request):
    return render(request, 'tarea/index.html')


class listar_tarea(LoginRequiredMixin, ListView):
    model = Tarea
    template_name = 'tarea/lista_tareas.html'
    context_object_name = 'listar_tarea'
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
        return super(listar_tarea, self).dispatch(request,*args,**kwargs)


class crear_tarea(LoginRequiredMixin, CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tarea/proyecto_form.html'
    success_url = reverse_lazy('listar_tarea')
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            def controlador(request):
                try:
                    user_rol = Rol.objects.values_list('choices', flat=True).get(pk=request.user.rol.get_id())
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
        return super(crear_tarea, self).dispatch(request,*args,**kwargs)

    def get_form_kwargs(self):
        kwargs = super(crear_tarea, self).get_form_kwargs()
        # get users, note: you can access request using: self.request
        kwargs['Tarea'] = Tarea
        return kwargs


class eliminar_tarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    template_name = 'tarea/proyecto_delete.html'
    success_url = reverse_lazy('listar_tarea')
    context_object_name = 'eliminar_tarea'
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
        return super(eliminar_tarea, self).dispatch(request,*args,**kwargs)


class editar_tarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    fields = ['version', 'prioridad', 'estado', 'descripcion', 'observacion', 'id_tarea_padre', 'id_proyecto']
    template_name = 'tarea/proyecto_form.html'
    success_url = reverse_lazy('listar_tarea')
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
        return super(editar_tarea, self).dispatch(request,*args,**kwargs)
