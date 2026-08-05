from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import Product


class ProductListView(PermissionRequiredMixin, ListView):
    model = Product
    template_name = 'products/products-list.html'
    context_object_name = 'products'
    permission_required = 'products.view_product'


class ProductDetailView(PermissionRequiredMixin, DetailView):
    model = Product
    template_name = 'products/products-detail.html'
    permission_required = 'products.view_product'


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    fields = '__all__'
    template_name = 'products/products-create.html'
    success_url = reverse_lazy('products:list')
    permission_required = 'products.add_product'


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'products/products-edit.html'
    success_url = reverse_lazy('products:list')
    permission_required = 'products.change_product'


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/products-delete.html'
    success_url = reverse_lazy('products:list')
    permission_required = 'products.delete_product'
