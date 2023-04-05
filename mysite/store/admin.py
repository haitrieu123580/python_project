from django.contrib import admin

# Register your models here.
from .models import Account, Customer, Card, CartItem, Brand, Laptop, Image
admin.site.register(Account)
admin.site.register(Customer)
admin.site.register(Card)
admin.site.register(CartItem)
admin.site.register(Brand)
admin.site.register(Laptop)
admin.site.register(Image)
