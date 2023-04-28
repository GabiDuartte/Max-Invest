from django.db import models

# Create your models here.

class Investor(models.Model):
    nome = models.CharField(max_length=200)
    #login, perfis(conservador, moderado, arrojado)

class Stock(models.Model):
    cod_ativo = models.CharField(max_length=6)
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=200)
    quantidade = models.DecimalField(max_digits=15, decimal_places=0)
    valor_total = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.nome

class Transaction(models.Model):
    ESCOLHA = (
        ("C", "Compra"),
        ("V", "Venda")
    )

    data = models.DateTimeField('Data', auto_now_add=True)
    stock = models.ManyToOneRel(Stock, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=0)
    preço = models.DecimalField(max_digits=15, decimal_places=2)
    tipo = models.CharField(max_length=1, choices=ESCOLHA, blank=False, null=False)
    corretagem = models.DecimalField(max_digits=8,default=0)
    investor = models.ManyToOneRel(Investor, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo

    def positivo(n):
        if n > 0:
            print(n)
        else:
            print('Erro')
    

