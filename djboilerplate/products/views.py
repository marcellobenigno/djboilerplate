from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProductForm
from .models import Product


def list(request):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list,
    }
    return render(request, 'products/list.html', context)


def create(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto criado com sucesso!')
            return redirect('products:list')

    context = {
        'form': form,
    }
    return render(request, 'products/form.html', context)


def detail(request, pk):
    obj = get_object_or_404(Product, pk=pk)

    context = {
        'obj': obj,
    }
    return render(request, 'products/detail.html', context)


def update(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=obj)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto editado com sucesso!')
            return redirect('products:list')

    context = {
        'form': form,
    }
    return render(request, 'products/form.html', context)


def delete(request, pk):
    obj = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Produto deletado com sucesso!')
        return redirect('products:list')

    context = {
        'obj': obj,
    }
    return render(request, 'products/delete.html', context)
