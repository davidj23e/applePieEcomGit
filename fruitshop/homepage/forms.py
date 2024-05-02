# forms.py

from django import forms
from .models import FruitInventory

class FruitInventoryForm(forms.ModelForm):
    item_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    item_price = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tagline = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = FruitInventory
        fields = ['item_name', 'item_price', 'tagline', 'image']
        labels = {
            'item_name': 'Fruit Name',
            'item_price': 'Price',
            'tagline': 'Tagline',
        }
        
