from django.db.models import Count, Sum, OuterRef, Subquery, F, Q, Case, When, Value
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import Ad
from leads.models import Lead
from customers.models import Customer
from contracts.models import Contract


class AdListView(PermissionRequiredMixin, ListView):
    model = Ad
    template_name = 'ads/ads-list.html'
    context_object_name = 'ads'
    permission_required = 'ads.view_ad'


class AdDetailView(PermissionRequiredMixin, DetailView):
    model = Ad
    template_name = 'ads/ads-detail.html'
    permission_required = 'ads.view_ad'


class AdCreateView(PermissionRequiredMixin, CreateView):
    model = Ad
    fields = '__all__'
    template_name = 'ads/ads-create.html'
    success_url = reverse_lazy('ads:list')
    permission_required = 'ads.add_ad'


class AdUpdateView(PermissionRequiredMixin, UpdateView):
    model = Ad
    fields = '__all__'
    template_name = 'ads/ads-edit.html'
    success_url = reverse_lazy('ads:list')
    permission_required = 'ads.change_ad'


class AdDeleteView(PermissionRequiredMixin, DeleteView):
    model = Ad
    template_name = 'ads/ads-delete.html'
    success_url = reverse_lazy('ads:list')
    permission_required = 'ads.delete_ad'


class AdStatisticView(PermissionRequiredMixin, ListView):
    model = Ad
    template_name = 'ads/ads-statistic.html'
    context_object_name = 'ads'
    permission_required = 'ads.view_ad'

    def get_queryset(self):
        # Аннотируем каждый Ad количеством лидов и активных клиентов,
        # а также отношением общей суммы контрактов к бюджету.
        leads_count = Lead.objects.filter(ad=OuterRef('pk')).values('ad').annotate(cnt=Count('id')).values('cnt')
        customers_count = Customer.objects.filter(customer__ad=OuterRef('pk')).values('customer__ad').annotate(cnt=Count('id')).values('cnt')
        # Общая сумма контрактов для клиентов, пришедших через эту рекламную кампанию
        total_contract_cost = Contract.objects.filter(
            customer__customer__ad=OuterRef('pk')
        ).values('customer__customer__ad').annotate(sum=Sum('cost')).values('sum')

        return Ad.objects.annotate(
            leads_count=Subquery(leads_count, output_field=models.IntegerField()),
            customers_count=Subquery(customers_count, output_field=models.IntegerField()),
            total_contract_sum=Subquery(total_contract_cost, output_field=models.DecimalField(max_digits=10, decimal_places=2))
        ).annotate(
            profit=Case(
                When(budget__gt=0, then=F('total_contract_sum') - F('budget')),
                default=Value(None),
                output_field=models.DecimalField(max_digits=10, decimal_places=2)
            )
        )
