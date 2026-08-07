from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from .models import Lead
from customers.models import Customer
from customers.forms import CustomerForm  # создадим форму позже


class LeadListView(PermissionRequiredMixin, ListView):
    model = Lead
    template_name = 'leads/leads-list.html'
    context_object_name = 'leads'
    permission_required = 'leads.view_lead'


class LeadDetailView(PermissionRequiredMixin, DetailView):
    model = Lead
    template_name = 'leads/leads-detail.html'
    permission_required = 'leads.view_lead'


class LeadCreateView(PermissionRequiredMixin, CreateView):
    model = Lead
    fields = '__all__'
    template_name = 'leads/leads-create.html'
    success_url = reverse_lazy('leads:list')
    permission_required = 'leads.add_lead'


class LeadUpdateView(PermissionRequiredMixin, UpdateView):
    model = Lead
    fields = '__all__'
    template_name = 'leads/leads-edit.html'
    success_url = reverse_lazy('leads:list')
    permission_required = 'leads.change_lead'


class LeadDeleteView(PermissionRequiredMixin, DeleteView):
    model = Lead
    template_name = 'leads/leads-delete.html'
    success_url = reverse_lazy('leads:list')
    permission_required = 'leads.delete_lead'


class LeadToCustomerView(PermissionRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customers-create.html'
    permission_required = 'customers.add_customer'

    def get_initial(self):
        initial = super().get_initial()
        lead_id = self.kwargs.get('pk')
        lead = get_object_or_404(Lead, pk=lead_id)
        initial['customer'] = lead
        return initial

    def get_success_url(self):
        return reverse_lazy('customers:list')
