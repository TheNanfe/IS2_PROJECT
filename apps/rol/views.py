from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.rol.models import Rol
from apps.rol.forms import RegistroRol
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

PERMISO_CREATE = 'rol_cre'
PERMISO_LIST = 'rol_list'
PERMISO_EDIT = 'rol_edit'
PERMISO_DELETE = 'rol_del'


class RegistroRol(CreateView):
    model = Rol
    template_name = "rol/usuario_form.html"
    form_class = RegistroRol
    success_url = reverse_lazy("listar_rol")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            def controlador(request):
                try:
                   user_rol = Rol.objects.values_list('choices', flat=True).get(pk=str(request.user.rol))
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
        return super(RegistroRol, self).dispatch(request,*args,**kwargs)

    def form_valid(self, form):
        permisos = form.cleaned_data['Permisos']
        form.instance.choices = permisos
        return super(RegistroRol,self).form_valid(form)


class RolList(ListView):
    model = Rol
    template_name = 'rol/lista_roles.html'
    context_object_name = 'rol_list'
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            def controlador(request):
                try:
                    user_rol = Rol.objects.values_list('choices', flat=True).get(pk=str(request.user.rol))
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
        return super(RolList , self).dispatch(request,*args,**kwargs)


class EditarRol(UpdateView):
    model = Rol
    fields = ['nombre', 'descripcion', 'choices']
    template_name = 'rol/rol_form.html'
    success_url = reverse_lazy("listar_rol")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            def controlador(request):
                try:
                   user_rol = Rol.objects.values_list('choices', flat=True).get(pk=str(request.user.rol))
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
        return super(EditarRol, self).dispatch(request,*args,**kwargs)


class RolDelete(DeleteView):
    model = Rol
    template_name = 'rol/rol_delete.html'
    success_url = reverse_lazy('listar_rol')
    context_object_name = 'rol_delete'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            def controlador(request):
                try:
                   user_rol = Rol.objects.values_list('choices', flat=True).get(pk=str(request.user.rol))
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
        return super(RolDelete, self).dispatch(request,*args,**kwargs)
