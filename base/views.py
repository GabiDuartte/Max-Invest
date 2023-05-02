from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Investment

class Login(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('investments')

class Register(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('investments')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('investments')
        return super(Register, self).get(*args, **kwargs)

class InvestList(LoginRequiredMixin, ListView):
    model = Investment
    context_object_name = 'investments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['investments'] = context['investments'].filter(user=self.request.user)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['investments'] = context['investments'].filter(code__icontains=search_input)
        return context

class InvestCreate(LoginRequiredMixin, CreateView):
    model = Investment
    fields = ['code', 'date', 'value', 'amount', 'brokerage', 'taxab3']
    success_url = reverse_lazy('investments')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(InvestCreate, self).form_valid(form)

class InvestUpdate(LoginRequiredMixin, UpdateView):
    model = Investment
    fields = ['code', 'date', 'value', 'amount', 'brokerage', 'taxab3']
    success_url = reverse_lazy('investments')

class InvestDelete(LoginRequiredMixin, DeleteView):
    model = Investment
    context_object_name = 'investment'
    success_url = reverse_lazy('investments')