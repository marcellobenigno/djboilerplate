from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProductForm
from .models import Product


@login_required
def list(request):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list,
    }
    return render(request, 'products/list.html', context)


@login_required
def create(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Produto criado com sucesso!')
        return redirect('products:list')

    context = {
        'form': form,
    }
    return render(request, 'products/form.html', context)


@login_required
def detail(request, pk):
    obj = get_object_or_404(Product, pk=pk)

    context = {
        'obj': obj,
    }
    return render(request, 'products/detail.html', context)


@login_required
def update(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None,
                       request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Produto editado com sucesso!')
        return redirect('products:list')

    context = {
        'form': form,
    }
    return render(request, 'products/form.html', context)


@login_required
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
