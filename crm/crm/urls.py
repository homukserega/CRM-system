"""
URL configuration for crm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import IndexView

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from rest_framework.routers import DefaultRouter
from ads.views import AdViewSet
from contracts.views import ContractViewSet
from customers.views import CustomerViewSet
from leads.views import LeadViewSet
from products.views import ProductViewSet

router = DefaultRouter()
router.register(r'ads', AdViewSet)
router.register(r'contracts', ContractViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'leads', LeadViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', IndexView.as_view(), name='home'),
    path('products/', include('products.urls')),
    path('ads/', include('ads.urls')),
    path('leads/', include('leads.urls')),
    path('contracts/', include('contracts.urls')),
    path('customers/', include('customers.urls')),
]

if settings.DEBUG:
    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # urlpatterns.append(
    #     path('__debug__/', include('debug_toolbar.urls')),
    # )
