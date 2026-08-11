from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from customers.forms import CustomerForm  # создадим форму позже
from customers.models import Customer

from .models import Lead
from .serializers import LeadSerializer


@extend_schema(tags=["leads"])
class LeadViewSet(ModelViewSet):
    """
    Управление потенциальными клиентами.
    - Создание, просмотр, изменение и удаление потенциальных клиентов.
    - Поля: Имя, фамилия, телефон, email, рекламная кампания, из которой он узнал об услуге.
    """

    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    http_method_names = ["get", "post", "put", "delete"]
    permission_classes = [DjangoModelPermissions]

    @extend_schema(
        examples=[
            OpenApiExample(
                'Создание Потенциального клиента',
                value={
                    "first_name": 'Имя',
                    "last_name": "Фамилия",
                    "phone": "5000000",
                    "email": "example@enmail.com",
                }, request_only=True,
            )
        ]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        examples=[
            OpenApiExample(
                'Обновление Потенциального клиента',
                value={
                    "first_name": 'Имя',
                }, request_only=True,
            )
        ]
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class LeadListView(PermissionRequiredMixin, ListView):
    model = Lead
    template_name = "leads/leads-list.html"
    context_object_name = "leads"
    permission_required = "leads.view_lead"


class LeadDetailView(PermissionRequiredMixin, DetailView):
    model = Lead
    template_name = "leads/leads-detail.html"
    permission_required = "leads.view_lead"


class LeadCreateView(PermissionRequiredMixin, CreateView):
    model = Lead
    fields = "__all__"
    template_name = "leads/leads-create.html"
    success_url = reverse_lazy("leads:list")
    permission_required = "leads.add_lead"


class LeadUpdateView(PermissionRequiredMixin, UpdateView):
    model = Lead
    fields = "__all__"
    template_name = "leads/leads-edit.html"
    success_url = reverse_lazy("leads:list")
    permission_required = "leads.change_lead"


class LeadDeleteView(PermissionRequiredMixin, DeleteView):
    model = Lead
    template_name = "leads/leads-delete.html"
    success_url = reverse_lazy("leads:list")
    permission_required = "leads.delete_lead"


class LeadToCustomerView(PermissionRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers/customers-create.html"
    permission_required = "customers.add_customer"

    def get_initial(self):
        initial = super().get_initial()
        lead_id = self.kwargs.get("pk")
        lead = get_object_or_404(Lead, pk=lead_id)
        initial["lead"] = lead
        return initial

    def get_success_url(self):
        return reverse_lazy("customers:list")
