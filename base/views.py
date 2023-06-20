from django.shortcuts import redirect, render
from django import forms
<<<<<<< HEAD
from django.contrib.auth import get_user_model
=======
>>>>>>> ce8105a2c2caf77c6b45a38385f45c431e81e277
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.core.paginator import Paginator
from django.forms import widgets
from django.utils import timezone
<<<<<<< HEAD
import requests
'''from .forms import UserCreationForm'''
from .models import Investment,Stock, Investor
from. serializers import InvestorSerializer, InvestmentSerializer, StockSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view

User = get_user_model()
=======

import requests
from .models import Investment,Stock
>>>>>>> ce8105a2c2caf77c6b45a38385f45c431e81e277

class Login(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('investments')

class Register(FormView):
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
    
    def create_user(request):
        if request.method == 'POST':
<<<<<<< HEAD
            form = UserCreationForm(request.POST)
=======
            form = UserCreationForm(request.post)
>>>>>>> ce8105a2c2caf77c6b45a38385f45c431e81e277
            if form.is_valid():
                user = form.save(commit=False)
                user.perfil = form.cleaned_data['Role']
                user.save()
                return redirect('home')
            else:
                form = UserCreationForm()
<<<<<<< HEAD
        return render(request, 'register.html', {'form': form})

    @staticmethod  
    @api_view(['GET'])
    def getData1(request):
        perfis = Investor.objects.all()
        serializer  = InvestorSerializer(perfis, many=True)
        return Response(serializer.data)
    
    @staticmethod
    @api_view(['POST'])
    def addPerfil(request):
        serializer = InvestorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

=======
            return render(request, 'register.html', {'form': form})

    
>>>>>>> ce8105a2c2caf77c6b45a38385f45c431e81e277

class StocksList(LoginRequiredMixin, ListView):
    model = Stock
    template_name = 'stocks_list.html'
    context_object_name = 'stocks'
    paginate_by = 10 # exibe 10 itens por página

    def get_queryset(self):
        available_stocks = []
        response = requests.get('https://brapi.dev/api/quote/list')
        if response.status_code == 200:
            available_stocks = response.json()['stocks']
        queryset = Stock.objects.filter(stock__in=[s['stock'] for s in available_stocks])
        return queryset.order_by('stock')

<<<<<<< HEAD
    @staticmethod
    @api_view(['GET'])
    def getData(request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)

    @staticmethod
    @api_view(['POST'])
    def addStock(request):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
=======

>>>>>>> ce8105a2c2caf77c6b45a38385f45c431e81e277

class InvestList(LoginRequiredMixin, ListView):
    model = Investment
    context_object_name = 'investments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['investments'] = context['investments'].filter(user=self.request.user)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['investments'] = context['investments'].filter(stock__icontains=search_input)
        return context
    
class InvestDetail(LoginRequiredMixin, DetailView):
    model = Investment
    context_object_name = 'investment'


class InvestForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = ['stock', 'date', 'value', 'amount', 'brokerage', 'type']

    stock = forms.ModelChoiceField(queryset=Stock.objects.all())
    date = forms.DateField(widget=widgets.DateInput(attrs={'type': 'date'}), initial=timezone.now)

    def get_available_stocks(self):
        available_stocks = []
        response = requests.get('https://brapi.dev/api/quote/list')
        if response.status_code == 200:
            available_stocks = response.json()['stocks']
        available_stocks = Stock.objects.filter(stock__in=[s['stock'] for s in available_stocks])
        return available_stocks

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].queryset = Stock.objects
        self.fields['stock'].label = 'Ação'
        self.fields['stock'].empty_label = None


class InvestCreate(LoginRequiredMixin, CreateView):
    model = Investment
    form_class = InvestForm
    success_url = reverse_lazy('investments')
    template_name = 'base/investment_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(InvestCreate, self).form_valid(form)
<<<<<<< HEAD
        
=======
>>>>>>> ce8105a2c2caf77c6b45a38385f45c431e81e277

class InvestUpdate(LoginRequiredMixin, UpdateView):
    model = Investment
    form_class = InvestForm
    success_url = reverse_lazy('investments')
    template_name = 'base/investment_form.html'


class InvestDelete(LoginRequiredMixin, DeleteView):
    model = Investment
    context_object_name = 'investment'
    success_url = reverse_lazy('investments')