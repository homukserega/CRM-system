from django.contrib import admin

from .models import Ad


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "product", "promotion", "budget")
    list_display_links = ("name",)
    search_fields = ("name", "promotion")
    list_filter = ("product", "budget")
    autocomplete_fields = ("product",)  # удобно, если много продуктов
