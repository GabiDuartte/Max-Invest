from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
# Create your models here.

class Investor(models.Model):
    Perfil_Risco = (
        ("1", "Conservador"),
        ("2", "Moderado"),
        ("3", "Arrojado")
    )
    perfil = models.CharField(max_length=20, choices=Perfil_Risco, default='1', null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.perfil

class Stock(models.Model):
    cod_ativo = models.CharField(max_length=6)
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=20)
    
    def __str__(self):
       return self.nome

class Investment(models.Model):
     choices = (
        ("C", "Compra"),
        ("V", "Venda")
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    code = models.CharField(verbose_name='Código',max_length=200)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Data de Investimento')
    type = models.CharField(verbose_name='Tipo',max_length=1, choices=choices, default='C', null=False)
    value = models.DecimalField(verbose_name='Valor Unitário',max_digits=15,decimal_places=2,default=0,validators=[MinValueValidator(0)])
    amount = models.IntegerField(verbose_name='Quantidade',default=0,validators=[MinValueValidator(0)])
    brokerage = models.DecimalField(verbose_name='Corretagem',max_digits=5,decimal_places=2,default=0,validators=[MinValueValidator(0)])
    taxab3 = models.DecimalField(verbose_name='Taxa B3',max_digits=5,decimal_places=2,default=0)

    def __str__(self):
        return self.code
    
    # taxa = 0,0325%

    class Meta:
        ordering = ['date']
        
    def valor_total(self):
        return self.amount * self.value 
    
    def taxas_totais(self):
        return self.taxab3 + self.brokerage 
    
    def valor_final(self):
        if self.type == 'C':
            return (self.amount * self.value)  + (self.taxab3 + self.brokerage)
        if self.type == 'V':
            return (self.amount * self.value) - (self.taxab3 + self.brokerage)
