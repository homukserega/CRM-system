from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'contract')
    list_display_links = ('customer',)
    search_fields = ('customer__last_name', 'customer__first_name', 'customer__email')
    list_filter = ('contract',)
    autocomplete_fields = ('customer', 'contract')