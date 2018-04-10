from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProductForm
from .models import Product


def list_(request):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list,
    }
    return render(request, 'products/list.html', context)


def create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('products:list')

    context = {
        'form': form,
    }
    return render(request, 'products/form.html', context)


def update(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('products:list')

    context = {
        'form': form,
    }
    return render(request, 'products/form.html', context)


def delete(request, pk):
    obj = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        obj.delete()
        return redirect('products:list')

    context = {
        'obj': obj,
    }
    return render(request, 'products/delete.html', context)
