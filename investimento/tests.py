from django.test import TestCase
import datetime
from django.utils import timezone
# Create your tests here.

from .models import Investimento, Calculo

def createInvest(id,code,days,amount,value,brokerage):
    time = timezone.now() + datetime.timedelta(days=days)
    return Investimento.objects.create(id=id,code=code,date=time,amount=amount,value=value,brokerage=brokerage)


