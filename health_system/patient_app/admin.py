from django.contrib import admin
from .models import (
    Country,
    Province,
    Town,
    MedicalInformation,
    Diagnosis,
    Patient,
    PatientImage,
)


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


@admin.register(MedicalInformation)
class MedicalInformationAdmin(admin.ModelAdmin):
    list_display = ("countries", "provinces", "towns", "hospital")
    search_fields = ("countries", "provinces", "towns", "hospital")
    list_filter = ("countries", "provinces", "towns", "hospital")


@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ("hospitals", "diagnosis")
    search_fields = ("hospitals", "diagnosis")
    list_filter = ("hospitals", "diagnosis")


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        "auto_id",
        "first_name",
        "last_name",
        "date_of_birth",
        "gender",
        "email",
        "phone_number",
        "created_at",
        "updated_at",
    )
    search_fields = ("first_name", "last_name", "email", "phone_number")
    list_filter = ("gender", "created_at", "updated_at")


@admin.register(PatientImage)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("patient", "image", "description", "uploaded_at")
    search_fields = ("patient__first_name", "patient__last_name", "description")
    list_filter = ("uploaded_at",)
