from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cost', 'description_preview')
    list_display_links = ('name',)
    search_fields = ('name', 'description')
    list_filter = ('cost',)
    fields = ('name', 'description', 'cost')
    readonly_fields = ('id',)

    def description_preview(self, obj):
        if obj.description and len(obj.description) > 50:
            return obj.description[:50] + '…'
        return obj.description
    description_preview.short_description = 'Описание (кратко)'
