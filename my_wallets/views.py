from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import generic
from . models import Investor, Stock, Transaction
# Create your views here.

class HomeView(generic.ListView):
    template_name = 'my_wallet/dashboard.html'
    
    def criar_transacao(request):
        if request.method == 'POST':
            form = Transaction(request.POST)
            if form.is_valid():
                form.save()
                return redirect('')
            else:
                form = Transaction()
        return render(request, 'dashboard.html', {'form': form})

class DetailView(generic.DetailView):
    model = Transaction
    template_name = 'my_wallet/detail.html'

    def get_queryset(self):
        return Transaction.objects.filter(
            data__ltde = timezone.now()
        )
    
    def detalhe(request, id):
        transacao = get_object_or_404(Transaction, pk=id)
        if request.method == 'POST':
            if 'excluir' in request.POST:
                transacao.delete()
                return redirect('detalhes', id=id)
            else:
                raise Exception('Erro')
        else:
            form = Transaction(isinstance=transacao)
        return render(request, 'detalhe.html', {'transscao': transacao})
    
class ResultsView(generic.DetailView):
    model = Transaction
    template_name = 'my_wallet/transaction.html'
    
    def listar(request):
        operacoes = Transaction.objects.order_by('data')
        return render(request, 'transactions.html', {'operacoes': operacoes})



    
