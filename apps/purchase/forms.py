from django import forms
from django.forms import ModelForm
from .models import Purchase

class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = ['title','amount', 'email']


        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'amount': forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
    }



    
