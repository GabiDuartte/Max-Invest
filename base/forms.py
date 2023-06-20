from django import forms
from .models import Investor, Perfil_Risco

class UserCreationForm(forms.ModelForm):
    perfil = forms.ChoiceField(choices=Perfil_Risco)
  
    class Meta:
        model = Investor
        fields = [
             'perfil',
        ]
