from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView, RedirectView
from apps.usuario.forms import RegistroForm
from apps.usuario.decorator import *

PERMISO_VISTA_USER = ['administrador', '123']


class RegistroForm(CreateView):
    model = User
    template_name = "usuario/usuario_form.html"
    form_class = RegistroForm
    success_url = reverse_lazy("listar_usuario")

    def dispatch(self, request, *args, **kwargs):
        def controlador(request):
            if str(request.user.rol) in PERMISO_VISTA_USER:
                print('felicidades')
                return 0
            else:
                print(request.user.rol)
                return 1

        if controlador(request) == 1:
            return HttpResponseRedirect(reverse_lazy('index'))

        return super(RegistroForm, self).dispatch(request, *args, **kwargs)


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "core/login.html"
    success_url = reverse_lazy("index")

    def dispatch(self, request, *args, **kwargs):
        print(args)
        print(kwargs)
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    pattern_name = 'login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class LoginRequiredMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('login'))
        else:
            return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class UsuarioList(LoginRequiredMixin, ListView):
    model = User
    template_name = 'usuario/lista_usuarios.html'
    context_object_name = 'user_list'
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        def controlador(request):
            if str(request.user.rol) in PERMISO_VISTA_USER:
                print('felicidades')
                return 0
            else:
                print(request.user.rol)
                return 1

        if controlador(request) == 1:
            return HttpResponseRedirect(reverse_lazy('index'))

        return super(UsuarioList, self).dispatch(request, *args, **kwargs)


class editarUsuario(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    template_name = 'usuario/usuario_form.html'
    success_url = reverse_lazy("listar_usuario")

    def dispatch(self, request, *args, **kwargs):
        def controlador(request):
            if str(request.user.rol) in PERMISO_VISTA_USER:
                print('felicidades')
                return 0
            else:
                print(request.user.rol)
                return 1

        if controlador(request) == 1:
            return HttpResponseRedirect(reverse_lazy('index'))

        return super(editarUsuario, self).dispatch(request, *args, **kwargs)


"""def editarUsuario(request, pk):
    usuario = User.objects.get(id=pk)
    if request.method == 'GET':
        usuario_form = RegistroForm(instance=usuario)
    else:
        usuario_form = RegistroForm(request.POST, instance=usuario)
        if usuario_form.is_valid():
            return redirect('lista_usuario')
        else:
            usuario_form = RegistroForm()
    return render(request, 'usuario/usuario_form.html', {'form': usuario_form})"""


class UsuarioDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'usuario/usuario_delete.html'
    success_url = reverse_lazy('listar_usuario')
    context_object_name = 'usuario_delete'

    def dispatch(self, request, *args, **kwargs):
        def controlador(request):
            if str(request.user.rol) in PERMISO_VISTA_USER:
                print('felicidades')
                return 0
            else:
                print(request.user.rol)
                return 1

        if controlador(request) == 1:
            return HttpResponseRedirect(reverse_lazy('index'))

        return super(UsuarioDelete, self).dispatch(request, *args, **kwargs)
