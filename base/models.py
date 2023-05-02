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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    code = models.CharField(verbose_name='Código',max_length=200)
    stock = models.ManyToOneRel(Stock, on_delete=models.CASCADE)
    investor = models.ManyToOneRel(Investor, on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Data de Investimento')
    value = models.DecimalField(verbose_name='Valor Unitário',max_digits=15,decimal_places=2,default=0,validators=[MinValueValidator(0)])
    amount = models.IntegerField(verbose_name='Quantidade',default=0,validators=[MinValueValidator(0)])
    brokerage = models.DecimalField(verbose_name='Corretagem',max_digits=5,decimal_places=2,default=0,validators=[MinValueValidator(0)])
    taxab3 = models.DecimalField(verbose_name='Taxa B3',max_digits=5,decimal_places=2,default=0)

    def __str__(self):
        return self.code
    
    # taxa = 0,0325%

    class Meta:
        ordering = ['date']
