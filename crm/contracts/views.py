from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from .forms import ContractForm
from .models import Contract
from .serializers import ContractSerializer


@extend_schema(tags=["contracts"])
class ContractViewSet(ModelViewSet):
    """
    Управление контрактами.
    - Создание, просмотр, изменение и удаление контрактов.
    - Поля: название, предоставляемая услуга, файл с документом,
    дата заключения, период действия, сумма
    """

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    http_method_names = ["get", "post", "put", "delete"]


class ContractListView(PermissionRequiredMixin, ListView):
    """Список контрактов."""

    model = Contract
    template_name = "contracts/contracts-list.html"
    context_object_name = "contracts"
    permission_required = "contracts.view_contract"


class ContractDetailView(PermissionRequiredMixin, DetailView):
    """Детали контракта."""

    model = Contract
    template_name = "contracts/contracts-detail.html"
    permission_required = "contracts.view_contract"


class ContractCreateView(PermissionRequiredMixin, CreateView):
    """Создание контракта."""

    model = Contract
    form_class = ContractForm
    template_name = "contracts/contracts-create.html"
    success_url = reverse_lazy("contracts:list")
    permission_required = "contracts.add_contract"


class ContractUpdateView(PermissionRequiredMixin, UpdateView):
    """Редактирование контракта."""

    model = Contract
    form_class = ContractForm
    template_name = "contracts/contracts-edit.html"
    success_url = reverse_lazy("contracts:list")
    permission_required = "contracts.change_contract"


class ContractDeleteView(PermissionRequiredMixin, DeleteView):
    """Удаление контракта."""

    model = Contract
    template_name = "contracts/contracts-delete.html"
    success_url = reverse_lazy("contracts:list")
    permission_required = "contracts.delete_contract"
