

from django.http import HttpResponse
from .models import Laptop, Brand, Image
from django.shortcuts import render, redirect, get_object_or_404
from .models import Laptop
from .forms import LaptopForm

def index(request):
    return render(request, 'index.html')
def lapList(request):
    lap_list = Laptop.objects.all()
    context = {'laptop_list': lap_list }
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
    if request.method == 'POST' :
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

