from django.contrib import admin

from .models import Country, Province, Town, InsuranceCompany


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("countries",)
    search_fields = ("countries",)
    list_filter = ("countries",)


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ("countries", "provinces")
    search_fields = ("countries", "provinces")
    list_filter = ("countries", "provinces")


@admin.register(Town)
class TownAdmin(admin.ModelAdmin):
    list_display = ("countries", "provinces", "towns")
    search_fields = ("countries", "provinces", "towns")
    list_filter = ("countries", "provinces", "towns")


@admin.register(InsuranceCompany)
class InusranceCompanyAdmin(admin.ModelAdmin):
    list_display = (
        "countries",
        "provinces",
        "towns",
        "name",
        "description",
        "address",
        "contact_number",
        "email",
        "website",
    )
    search_fields = ("name",)
    list_filter = ("countries", "provinces", "towns", "name")
