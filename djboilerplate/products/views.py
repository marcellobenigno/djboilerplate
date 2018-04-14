from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from .forms import ProductForm
from .models import Product


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    paginate_by = 5


class ProductDetail(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    model = Product


class ProductCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products:list')
    success_message = "Produto criado com sucesso!"


class ProductUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products:list')
    success_message = "Produto editado com sucesso!"


class ProductDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:list')
    success_message = "Produto deletado com sucesso!"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(ProductDelete, self).delete(request, *args, **kwargs)