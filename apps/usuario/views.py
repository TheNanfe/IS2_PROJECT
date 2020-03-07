from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import FormView, RedirectView

from apps.usuario.forms import RegistroForm
from apps.proyecto.urls import index


class RegistroForm(CreateView):
    model = User
    template_name = "registration/registro.html"
    form_class = RegistroForm
    success_url = reverse_lazy("index.html")


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "core/login.html"
    success_url = reverse_lazy("index.html")

    def dispatch(self, request, *args, **kwargs):
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
