from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Productos, Ordenes
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

# INDEX
@login_required
def index(request):
    orders = Ordenes.objects.all()
    products = Productos.objects.all()
    orders_count = orders.count()
    product_count=products.count()
    workers_count = User.objects.all().count()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form= OrderForm()
    context = {
        'orders' : orders,
        'form' : form,
        'products' : products,
        'product_count': product_count,
        'workers_count': workers_count,
        'orders_count': orders_count,
    }
    return render(request, 'dashboard/index.html', context)

# STAFF
@login_required
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    orders_count = Ordenes.objects.all().count()
    product_count= Productos.objects.all().count()
    context = {
        'workers': workers,
        'workers_count': workers_count,
        'orders_count' : orders_count,
        'product_count': product_count
    }
    return render(request, 'dashboard/staff.html',context)

# STAFF DETAIL
@login_required
def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers' : workers,
        
    }
    return render(request,'dashboard/staff_detail.html', context)


# PRODUCTS
@login_required
def products(request):
    items= Productos.objects.all() #Uso de ORM (Object Relational Mapping method)
    #items = Productos.objects.raw('SELECT * FROM dashboard_product')
    product_count = items.count()
    workers_count = User.objects.all().count()
    orders_count = Ordenes.objects.all().count()
    if request.method == 'POST':
        form= ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('nombre')
            messages.success(request, f'{product_name} fue añadido')
            return redirect('dashboard-products')
    else:
        form =ProductForm()
    context = {
        'items' : items,
        'form' : form,
        'workers_count' : workers_count,
        'orders_count' : orders_count,
        'product_count' : product_count
    }
    return render(request, 'dashboard/product.html', context)

# PRODUCT DELETE
@login_required
def product_delete(request, pk): 
    item = Productos.objects.get(id=pk)
    if request.method =='POST':
        item.delete()
        return redirect ('dashboard-products')
    return render(request, 'dashboard/product_delete.html')

 # PRODUCT UPDATE
@login_required
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

 # ORDER
@login_required
def order(request):
    orders = Ordenes.objects.all()
    orders_count = orders.count()
    workers_count = User.objects.all().count()
    product_count= Productos.objects.all().count()
    context = {
        'orders': orders,
        'workers_count': workers_count,
        'orders_count' : orders_count,
        'product_count' : product_count
    }
    return render(request, 'dashboard/order.html', context)