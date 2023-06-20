from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from django.contrib.auth.models import AbstractUser


class Investor(models.Model):
    Perfil = [
         ("1", "Conservador"),
         ("2", "Moderado"),
         ("3", "Arrojado")
    ]
           
    perfil = models.CharField(max_length=3, default="1", choices=Perfil)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    


class Stock(models.Model):
    stock = models.CharField(max_length=10, db_column='stock')
    name = models.CharField(max_length=200, db_column='name')
    market_cap = models.CharField(max_length=20, db_column='market_cap', null=True)
    
    def __str__(self):
       return self.stock

class Investment(models.Model):
    type_options = (
        ("C", "Compra"),
        ("V", "Venda")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, null=False)
    code = models.CharField(verbose_name='Código', max_length=25, null=False, blank=True)
    date = models.DateField(verbose_name='Data de Investimento')
    value = models.DecimalField(verbose_name='Valor Unitário',max_digits=15,decimal_places=2,default=0)
    amount = models.IntegerField(verbose_name='Quantidade',default=0)
    brokerage = models.DecimalField(verbose_name='Corretagem',max_digits=5,decimal_places=2,default=0)
    type = models.CharField(verbose_name='Tipo', max_length=1, choices=type_options, null=False, blank=True)

    def __str__(self):
        return self.code
    
    # taxa = 0,0325%
    def taxab3(self):
        return round(((self.value * self.amount) * Decimal(0.0325)), 2)
    
    def total_value(self):
        return self.value * self.amount
    
    def total_taxas(self):
        return round((self.brokerage + ((self.value * self.amount) * Decimal(0.0325))), 2)
    
    def total_final(self):
        if self.type == 'C':
            return round(((self.value * self.amount) + (self.brokerage + ((self.value * self.amount) * Decimal(0.0325)))), 2)
        if self.type == 'V':
            return round(((self.value * self.amount) - (self.brokerage + ((self.value * self.amount) * Decimal(0.0325)))), 2)
        
    def preco_medio(self):
        cont = 0
        pm = 0
        pm = ((cont*pm)+ self.total_final())/(cont + self.amount)

    def lucro_prejuizo(self):
        if self.type == 'V':
            return round(self.total_final() - (self.amount * self.preco_medio()), 2)

    class Meta:
        ordering = ['date']