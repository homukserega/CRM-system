from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import Contract
from .forms import ContractForm


class ContractListView(PermissionRequiredMixin, ListView):
    model = Contract
    template_name = 'contracts/contracts-list.html'
    context_object_name = 'contracts'
    permission_required = 'contracts.view_contract'


class ContractDetailView(PermissionRequiredMixin, DetailView):
    model = Contract
    template_name = 'contracts/contracts-detail.html'
    permission_required = 'contracts.view_contract'


class ContractCreateView(PermissionRequiredMixin, CreateView):
    model = Contract
    fields = ContractForm
    template_name = 'contracts/contracts-create.html'
    success_url = reverse_lazy('contracts:list')
    permission_required = 'contracts.add_contract'


class ContractUpdateView(PermissionRequiredMixin, UpdateView):
    model = Contract
    fields = ContractForm
    template_name = 'contracts/contracts-edit.html'
    success_url = reverse_lazy('contracts:list')
    permission_required = 'contracts.change_contract'


class ContractDeleteView(PermissionRequiredMixin, DeleteView):
    model = Contract
    template_name = 'contracts/contracts-delete.html'
    success_url = reverse_lazy('contracts:list')
    permission_required = 'contracts.delete_contract'
