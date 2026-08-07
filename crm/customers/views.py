from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import Customer
from .forms import CustomerForm


class CustomerListView(PermissionRequiredMixin, ListView):
    model = Customer
    template_name = 'customers/customers-list.html'
    context_object_name = 'customers'
    permission_required = 'customers.view_customer'


class CustomerDetailView(PermissionRequiredMixin, DetailView):
    model = Customer
    template_name = 'customers/customers-detail.html'
    permission_required = 'customers.view_customer'


class CustomerCreateView(PermissionRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customers-create.html'
    success_url = reverse_lazy('customers:list')
    permission_required = 'customers.add_customer'


class CustomerUpdateView(PermissionRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customers-edit.html'
    success_url = reverse_lazy('customers:list')
    permission_required = 'customers.change_customer'


class CustomerDeleteView(PermissionRequiredMixin, DeleteView):
    model = Customer
    template_name = 'customers/customers-delete.html'
    success_url = reverse_lazy('customers:list')
    permission_required = 'customers.delete_customer'