from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class Login(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')

class Index(LoginRequiredMixin, ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return 1