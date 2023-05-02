from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    code = models.CharField(verbose_name='Código',max_length=200)
    date = models.DateField(verbose_name='Data de Investimento')
    value = models.DecimalField(verbose_name='Valor Unitário',max_digits=15,decimal_places=2,default=0)
    amount = models.IntegerField(verbose_name='Quantidade',default=0)
    brokerage = models.DecimalField(verbose_name='Corretagem',max_digits=5,decimal_places=2,default=0)
    taxab3 = models.DecimalField(verbose_name='Taxa B3',max_digits=5,decimal_places=2,default=0)

    def __str__(self):
        return self.code
    
    # taxa = 0,0325%

    class Meta:
        ordering = ['date']