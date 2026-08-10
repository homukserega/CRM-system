from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models.deletion import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductSerializer


@extend_schema(tags=["products"])
class ProductViewSet(ModelViewSet):
    """
    Управление услугами.
    - Создание, просмотр, изменение и удаление услуг.
    - Поля: название, описание, стоимость.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ["get", "post", "put", "delete"]
    permission_classes = [DjangoModelPermissions]


class ProductListView(PermissionRequiredMixin, ListView):
    model = Product
    template_name = "products/products-list.html"
    context_object_name = "products"
    permission_required = "products.view_product"


class ProductDetailView(PermissionRequiredMixin, DetailView):
    model = Product
    template_name = "products/products-detail.html"
    permission_required = "products.view_product"


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    fields = "__all__"
    template_name = "products/products-create.html"
    success_url = reverse_lazy("products:list")
    permission_required = "products.add_product"


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    fields = "__all__"
    template_name = "products/products-edit.html"
    success_url = reverse_lazy("products:list")
    permission_required = "products.change_product"


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = "products/products-delete.html"
    success_url = reverse_lazy("products:list")
    permission_required = "products.delete_product"

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        try:
            obj.delete()
            messages.success(request, "Услуга успешно удалена.")
        except ProtectedError:
            messages.error(
                request,
                "Невозможно удалить услугу, "
                "так как она используется в рекламных кампаниях или контрактах. "
                "Сначала удалите или измените связанные записи."
            )
        return redirect(self.success_url)
