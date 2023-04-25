from django.db import models

# Create your models here.

class Investimento(models.Model):
    id = models.IntegerField(default=0)
    code = models.CharField(max_length=200)
    date = models.DateField('date published')
    amount = models.DecimalField(max_digits=5,decimal_places=0)
    value = models.DecimalField(max_digits=15,default=0)
    brokerage = models.DecimalField(default=0)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = u'Investimento'
        verbose_name_plural = u'INVESTIMENTOS'
        acao = ['-data']

class Calculo(models.Model):
    taxab3 = models.ManyToManyField(Investimento, verbose_name='Tarifa de Ações')
    amount = models.DecimalField(max_digits=5,decimal_places=0)
    valor = models.DecimalField(max_digits=15,decimal_places=2)
    subtotal = models.DecimalField(max_digits=10,decimal_places=2,editable=False)
    dt_invest = models.DateTimeField('Data do Investimento',auto_now_add=True)
    invest = models.ForeignKey(Investimento, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'Calculo'
        verbose_name_plural = u'Calculos'

    # taxa = 0,0325%
    def save(self,*args,**kwargs):
        self.subtotal = self.valor * self.amount
        self.invest.value += self.subtotal
        self.taxab3.values = (self.subtotal * 0.0325)/100 + self.subtotal
        
        return super(Calculo, self).save(*args, **kwargs)
