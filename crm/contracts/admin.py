from django.contrib import admin
from .models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product', 'cost', 'start_date', 'end_date', 'uploaded_at')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('product', 'start_date', 'end_date')
    autocomplete_fields = ('product',)
    date_hierarchy = 'start_date'
    readonly_fields = ('uploaded_at',)