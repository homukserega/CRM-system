from django.db.models import (
    Count, Sum, OuterRef, Subquery, F, Case,
    When, Value, IntegerField, DecimalField
)
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from leads.models import Lead
from customers.models import Customer

from .models import Ad


class AdListView(PermissionRequiredMixin, ListView):
    """Список рекламных кампаний."""
    model = Ad
    template_name = 'ads/ads-list.html'
    context_object_name = 'ads'
    permission_required = 'ads.view_ad'

    def get_queryset(self):
        # Аннотируем количеством лидов и клиентов
        leads_count = Lead.objects.filter(
            ad=OuterRef('pk')).values('ad').annotate(cnt=Count('id')).values('cnt')
        customers_count = Customer.objects.filter(
            customer__ad=OuterRef('pk')).values('customer__ad').annotate(cnt=Count('id')).values('cnt')
        return Ad.objects.annotate(
            leads_count=Subquery(leads_count, output_field=IntegerField()),
            customers_count=Subquery(customers_count, output_field=IntegerField())
        )


class AdDetailView(PermissionRequiredMixin, DetailView):
    """Детальная информация о рекламной кампании."""
    model = Ad
    template_name = 'ads/ads-detail.html'
    permission_required = 'ads.view_ad'


class AdCreateView(PermissionRequiredMixin, CreateView):
    """Создание рекламной кампании."""
    model = Ad
    fields = '__all__'
    template_name = 'ads/ads-create.html'
    success_url = reverse_lazy('ads:list')
    permission_required = 'ads.add_ad'


class AdUpdateView(PermissionRequiredMixin, UpdateView):
    """Редактирование рекламной кампании."""
    model = Ad
    fields = '__all__'
    template_name = 'ads/ads-edit.html'
    success_url = reverse_lazy('ads:list')
    permission_required = 'ads.change_ad'


class AdDeleteView(PermissionRequiredMixin, DeleteView):
    """Удаление рекламной кампании."""
    model = Ad
    template_name = 'ads/ads-delete.html'
    success_url = reverse_lazy('ads:list')
    permission_required = 'ads.delete_ad'


class AdStatisticView(PermissionRequiredMixin, ListView):
    """Статистика по рекламным кампаниям."""
    model = Ad
    template_name = 'ads/ads-statistic.html'
    context_object_name = 'ads'
    permission_required = 'ads.view_ad'

    def get_queryset(self):
        # Количество лидов
        leads_count = Lead.objects.filter(
            ad=OuterRef('pk')
        ).values('ad').annotate(cnt=Count('id')).values('cnt')

        # Количество активных клиентов
        customers_count = Customer.objects.filter(
            customer__ad=OuterRef('pk')
        ).values('customer__ad').annotate(cnt=Count('id')).values('cnt')

        # Общая сумма контрактов по клиентам этой кампании
        total_contract_cost = Customer.objects.filter(
            customer__ad=OuterRef('pk')
        ).values('customer__ad').annotate(
            total=Sum('contract__cost')
        ).values('total')

        return Ad.objects.annotate(
            leads_count=Subquery(leads_count, output_field=IntegerField()),
            customers_count=Subquery(customers_count, output_field=IntegerField()),
            total_contract_sum=Subquery(
                total_contract_cost,
                output_field=DecimalField(max_digits=10, decimal_places=2)
            )
        ).annotate(
            # Прибыль (доход - расход)
            profit=Case(
                When(budget__gt=0, then=F('total_contract_sum') - F('budget')),
                default=Value(None),
                output_field=DecimalField(max_digits=10, decimal_places=2)
            ),
            # Соотношение дохода к расходам (ROI)
            ratio=Case(
                When(budget__gt=0, then=F('total_contract_sum') / F('budget')),
                default=Value(None),
                output_field=DecimalField(max_digits=10, decimal_places=2)
            )
        )
