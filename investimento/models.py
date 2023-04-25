from django.db import models

# Create your models here.

class Investidor(models.Model):
    data = models.DateTimeField("Data")
    cod_ativo = models.CharField(max_length=200)
    quantidade = models.IntegerField(default=0)
    vlr_unitario = models.FloatField(default=0)
    corretagem = models.FloatField(default=0)

    def __str__(self):
        return self.cod_ativo

class Calculados(models.Model):
    qtd_acoes = models.ManyToManyField(Investidor, verbose_name='Quantidade de Ações')

    @property
    def valor_operacao():
        qtd_acoes = self.qtd_acoes.all()
        vlr_tot = 0.00
        for qtd_acao in qtd_acoes:
            vlr_tot += qtd_acao.vlr_unitario