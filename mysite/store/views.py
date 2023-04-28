

from django.http import HttpResponse
from .models import Laptop, Brand, Image
from account.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Laptop
from .forms import LaptopForm, ImageForm, UserForm, BrandForm
from account.forms import SignUpForm

from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy

class EditImageView(UpdateView):
    model = Image
    form_class = ImageForm
    template_name = 'edit_image.html'

    def form_valid(self, form):
        form.save()
        return redirect('view_images')


class DeleteImageView(DeleteView):
    model = Image
    template_name = 'delete_image.html'
    success_url = reverse_lazy('view_images')


def index(request):
    return render(request, 'base.html')


def lapList(request):
    lap_list = Laptop.objects.all()
    context = {'laptop_list': lap_list}
    return render(request, 'lapList.html', context)


def add_laptop(request):
    brands = Brand.objects.all()

    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            laptop = form.save()
            return redirect('lapList')
    else:
        form = LaptopForm()
    if form.errors:
        errors = form.errors
    else:
        errors = None

    return render(request, 'add_laptop.html', {'form': form, 'brands': brands, 'errors': errors})


def laptop_update(request, pk):

    laptop = get_object_or_404(Laptop, id=pk)
    if request.method == 'POST':
        form = LaptopForm(request.POST, instance=laptop)
        if form.is_valid():
            form.save()
            return redirect('lapList')
    else:
        form = LaptopForm(instance=laptop)

    return render(request, 'laptop_update.html', {'form': form})


def delete_laptop(request, pk):
    laptop = Laptop.objects.get(id=pk)
    if request.method == 'POST':
        laptop.delete()
        return redirect('lapList')
    context = {'item': laptop}
    return render(request, 'delete_laptop.html', context)


def laptop_detail(request, laptop_id):
    laptop = get_object_or_404(Laptop, id=laptop_id)
    images = Image.objects.filter(laptop=laptop)
    return render(request, 'laptop_detail.html', {'laptop': laptop, 'images': images})


def delete(request):
    # delete
    lapList()


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_images')
    else:
        form = ImageForm()
        laptops = Laptop.objects.all()
    return render(request, 'upload_image.html', {'form': form, 'laptops': laptops})


def view_images(request):
    laptops = Laptop.objects.all()
    images = []
    for laptop in laptops:
        images.append(Image.objects.filter(laptop=laptop))
    return render(request, 'view_images.html', {'laptops': laptops, 'images': images})

# CUSTOMER
def users_list(request):
    usersList =  User.objects.filter(is_customer = True)
    return render(request, 'users_list.html',{'usersList':usersList })
def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user_detail.html', {'user': user})

def user_update(request, pk):

    user = get_object_or_404(User, id=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        initial_role = 'Customer' if user.is_customer else 'Admin'
        form = UserForm(instance=user, initial={'role': initial_role})
    return render(request, 'user_update.html', {'form': form})


def user_delete(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('users')
    context = {'item': user}
    return render(request, 'user_delete.html', context)

def user_add(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return redirect('users')
    else:
        form = SignUpForm()
    if form.errors:
        errors = form.errors
    else:
        errors = None

    return render(request, 'user_add.html', {'form': form, 'errors': errors})

# Brand
def brand_list(request):
    brand_list =  Brand.objects.all()
    return render(request, 'brand_list.html',{'brand_list':brand_list })

def brand_detail(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    return render(request, 'brand_detail.html', {'brand': brand})

def brand_add(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            brand = form.save()
            return redirect('brand_list')
    else:
        form = BrandForm()
    if form.errors:
        errors = form.errors
    else:
        errors = None

    return render(request, 'brand_add.html', {'form': form, 'errors': errors})

def brand_update(request, brand_id):

    brand = get_object_or_404(Brand, id=brand_id)
    if request.method == 'POST':
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('brand_list')
    else:
        form = BrandForm(instance=brand)

    return render(request, 'brand_update.html', {'form': form})

def brand_delete(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    if request.method == 'POST':
        brand.delete()
        return redirect('brand_list')
    context = {'brand_id': brand}
    return render(request, 'brand_delete.html', context)

def delete(request):
    # delete
    brand_list()