from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse,HttpResponse
import json
import datetime
from store.models import Laptop, Image, Cart, CartItem
from account.models import User
from django.contrib.auth.decorators import login_required
from store.models import *
# Create your views here.
@login_required(login_url='login_view')
def shop(request):
    try:
        laptops = Laptop.objects.prefetch_related('images').all()
        cart = Cart.objects.filter(customer=request.user).first()
        if not cart:
            cart = Cart(customer=request.user, total = 0)
            cart.save() 
        # print(cart.id)
        context = {'laptops': laptops, 'cart':cart}
        return render(request, 'shopping.html', context)
    except:
        return redirect('login_view')

@login_required(login_url='login_view')
def cart_details(request, cart_id):
    if not request.user.is_customer:
        return redirect('login_view')
    else:
        cart = Cart.objects.get(customer=request.user)
        cart_item = CartItem.objects.filter(cart = cart_id )
        context = {'cart':cart, 'cart_item':cart_item}
        print(context)
        return render(request, 'cart_details.html', context) 

@login_required(login_url='login_view')
def add_to_cart(request, laptop_id):
    if not request.user.is_customer:
        return redirect('login_view')
    else:
        print(laptop_id)
        cart = Cart.objects.get(customer=request.user)
        laptop = get_object_or_404(Laptop, id=laptop_id)
        cart_item = CartItem.objects.create(cart = cart, laptop = laptop, price = laptop.price )
        cart_item.save()
        cart_item = CartItem.objects.filter(cart     = cart )
        context = {'cart':cart, 'cart_item':cart_item}
        return render(request, 'cart_details.html', context) 
    

