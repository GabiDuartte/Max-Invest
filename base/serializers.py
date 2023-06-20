from rest_framework import serializers
from .models import Investor, Stock, Investment

class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = ['perfil', 'user']

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class InvestmentSerializer(serializers.ModelSerializer):
    user = InvestorSerializer()
    Stock = StockSerializer()

    class Meta:
        model = Investment 
        fields = '__all__'