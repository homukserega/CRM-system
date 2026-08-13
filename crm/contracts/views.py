from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework.permissions import DjangoModelPermissions
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
    permission_classes = [DjangoModelPermissions]

    @extend_schema(
    examples=[
        OpenApiExample(
            'Один контракт в списке',
            value=({"name": 'Контракт 1',
                    "product": 1,
                    "file": "путь/к/файлу.doc",
                    "start_date": "2025-01-01",
                    "end_date": "2025-12-31",
                    "cost": 5000.30}),
            response_only=True,
            ),
        ]
    )

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
    examples=[
        OpenApiExample(
            'Один контракт',
            value={
                    "name": 'Контракт 1',
                    "product": 1,
                    "file": "путь/к/файлу.doc",
                    "start_date": "2025-01-01",
                    "end_date": "2025-12-31",
                    "cost": 5000.30,
            },
            response_only=True,
            ),
        ]
    )

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        examples=[
            OpenApiExample(
                'Создание контракта',
                value={
                    "name": 'Контракт 1',
                    "product": 1,
                    "file": "путь/к/файлу.doc",
                    "start_date": "2025-01-01",
                    "end_date": "2025-12-31",
                    "cost": 5000.30,
                }, request_only=True,
            )
        ]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        examples=[
            OpenApiExample(
                'Обновление контракта',
                value={
                    "cost": 6000.00,
                    "end_data": "2026-06-02"
                }, request_only=True,
            )
        ]
    )

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


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
