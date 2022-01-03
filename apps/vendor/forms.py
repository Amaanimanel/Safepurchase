from django import forms
from django.forms import ModelForm

from apps.product.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price']

        widgets = {
            'category': forms.Select(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
        }