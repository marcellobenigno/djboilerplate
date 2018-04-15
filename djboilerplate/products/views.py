from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from .forms import ProductForm
from .mixings import SearchMixin
from .models import Product


class ProductListView(LoginRequiredMixin, SearchMixin, ListView):
    model = Product
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_terms'] = self.request.GET.get('q')
        context['total_itens'] = self.get_queryset().count()
        return context


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
