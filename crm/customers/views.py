from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from .forms import CustomerForm
from .models import Customer
from .serializers import CustomerSerializer


@extend_schema(tags=["customers"])
class CustomerViewSet(ModelViewSet):
    """
    Управление активными клиентами.
    - Создание, просмотр, изменение и удаление активных клиентов.
    - Поля: данные о потенциальном клиенте, данные о контракте.
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    http_method_names = ["get", "post", "put", "delete"]
    permission_classes = [DjangoModelPermissions]


class CustomerListView(PermissionRequiredMixin, ListView):
    model = Customer
    template_name = "customers/customers-list.html"
    context_object_name = "customers"
    permission_required = "customers.view_customer"


class CustomerDetailView(PermissionRequiredMixin, DetailView):
    model = Customer
    template_name = "customers/customers-detail.html"
    permission_required = "customers.view_customer"


class CustomerCreateView(PermissionRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers/customers-create.html"
    success_url = reverse_lazy("customers:list")
    permission_required = "customers.add_customer"


class CustomerUpdateView(PermissionRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers/customers-edit.html"
    success_url = reverse_lazy("customers:list")
    permission_required = "customers.change_customer"


class CustomerDeleteView(PermissionRequiredMixin, DeleteView):
    model = Customer
    template_name = "customers/customers-delete.html"
    success_url = reverse_lazy("customers:list")
    permission_required = "customers.delete_customer"
