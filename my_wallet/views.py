from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from . models import Investor, Stock, Transaction
# Create your views here.

class HomeView(generic.ListView):
    template_name = 'my_wallet/dashboard.html'

class DetailView(generic.DetailView):
    model = Transaction
    template_name = 'my_wallet/detail.html'

    def get_queryset(self):
        return Transaction.objects.filter(
            data__ltde = timezone.now()
        )
class ResultsView(generic.DetailView):
    model = Transaction
    template_name = 'my_wallet/transaction.html'
    
        def listar(request):
        operacoes = Transaction.objects.order_by('data')
        return render(request, 'transactions.html', {'operacoes': operacoes})



    
