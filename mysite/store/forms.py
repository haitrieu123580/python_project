from django import forms
from .models import Laptop



class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ['name', 'brand', 'graphic_card', 'ram', 'cpu', 'screen_type', 'price']
