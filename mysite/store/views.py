from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Laptop

def index(request):
    return render(request, 'index.html')
def lapList(request):
    lap_list = Laptop.objects.all()
    context = {'laptop_list': lap_list }
    return render(request, 'lapList.html', context)