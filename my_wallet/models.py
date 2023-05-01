from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

 class Investor(models.Model):
    Perfil_Risco = (
        ("1", "Conservador"),
        ("2", "Moderado"),
        ("3", "Arrojado")
    )
    perfil = models.CharField(max_length=20, choices=Perfil_Risco, blank=False, null=False)
    #login

    def __str__(self):
        return self.perfil

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
    quantidade = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    preço = models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(0)])
    tipo = models.CharField(max_length=1, choices=ESCOLHA, blank=False, null=False)
    corretagem = models.DecimalField(max_digits=8,validators=[MinValueValidator(0)])
    investor = models.ManyToOneRel(Investor, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo
    

