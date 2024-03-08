from django.contrib import admin
from pharmacy_app.models import Pharmacy


@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "country",
        "province",
        "town",
        "location",
        "phone_number",
        "email",
    )
    search_fields = (
        "name",
        "country",
        "province",
        "town",
        "location",
    )
    list_filter = ("location",)
    ordering = ("name",)
