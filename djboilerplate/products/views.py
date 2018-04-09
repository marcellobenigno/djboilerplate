from django.shortcuts import render

from .models import Product


def list_(request):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list,
    }
    return render(request, 'products/list.html', context)
