from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Productos
from .forms import ProductForm

# Create your views here.


@login_required
def index(request):
    return render(request, 'dashboard/index.html')

@login_required
def staff(request):
    return render(request, 'dashboard/staff.html')

@login_required
def products(request):
    items= Productos.objects.all() #Uso de ORM (Object Relational Mapping method)
    #items = Productos.objects.raw('SELECT * FROM dashboard_product')
    
    if request.method == 'POST':
        form= ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    else:
        form =ProductForm()
    context = {
        'items' : items,
        'form' : form,
    }
    return render(request, 'dashboard/product.html', context)

def product_delete(request, pk): 
    item = Productos.objects.get(id=pk)
    if request.method =='POST':
        item.delete()
        return redirect ('dashboard-products')
    return render(request, 'dashboard/product_delete.html')

def product_update(request, pk):
    item = Productos.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    else:
        form = ProductForm(instance=item)
    context = {
        'form' : form,
    }
    return render(request, 'dashboard/product_update.html', context)


@login_required
def order(request):
    return render(request, 'dashboard/order.html')