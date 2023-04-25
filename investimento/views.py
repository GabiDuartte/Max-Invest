from django.shortcuts import render
from django.views import generic
from .models import Investimento, Calculo
# Create your views here.

class HomeView(generic.HomeView):
    def home (requests):
        return render(requests, 'investimento/index.html')

class CalcTot(generic.CalcTot):
    def total(request,id=None):
        context = {}
        context['total'] = Calculo.objects.get(id=id)
        return render(request, 'investimento/total.html',context)