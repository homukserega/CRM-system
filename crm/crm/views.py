from django.views.generic import TemplateView
from products.models import Product
from ads.models import Ad
from leads.models import Lead
from customers.models import Customer


class IndexView(TemplateView):
    template_name = 'users/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products_count'] = Product.objects.count()
        context['advertisements_count'] = Ad.objects.count()
        context['leads_count'] = Lead.objects.count()
        context['customers_count'] = Customer.objects.count()
        return context
