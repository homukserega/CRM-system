from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from ads.models import Ad
from customers.models import Customer
from leads.models import Lead
from products.models import Product


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'users/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Проверяем, есть ли у пользователя какие-либо права
        # get_all_permissions() возвращает множество всех разрешений
        # (включая унаследованные через группы)
        has_perms = bool(user.get_all_permissions())

        context['show_statistics'] = has_perms

        if has_perms:
            context['products_count'] = Product.objects.count()
            context['advertisements_count'] = Ad.objects.count()
            context['leads_count'] = Lead.objects.count()
            context['customers_count'] = Customer.objects.count()

        return context
