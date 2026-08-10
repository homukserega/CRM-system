from django.contrib import admin

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("id", "last_name", "first_name", "phone", "email", "ad")
    list_display_links = ("last_name",)
    search_fields = ("last_name", "first_name", "phone", "email")
    list_filter = ("ad",)
    autocomplete_fields = ("ad",)
