from django import forms
from .models import Laptop



class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ['name', 'brand', 'graphic_card', 'ram', 'cpu', 'screen_type', 'price']
    def clean_ram(self):
        ram = self.cleaned_data.get('ram')
        if not isinstance(ram, int):
            raise forms.ValidationError("RAM must be an integer")
        return ram
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero")
        return price