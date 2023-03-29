from django.shortcuts import render

# Create your views here.
def lap_detail(request, lap_id):
    # *todo: get lap by lap_id 
    # *! test with id = 1
    if lap_id==1:
        context = {
            'Id' : 'lap01',
            'Name': 'Macbook Pro 2022',
            'Brand': 'Apple',
            'Color': 'Black',
            'Card' : 'GTX',
            'Ram' : 16,
            'CPU': 'M1',
            'Screen_type':16,
            'Price': 30000000,
            # *! insert image urls of item
        }
    else:
        context={}
    return render(request, 'webApp/lap_detail.html', context)