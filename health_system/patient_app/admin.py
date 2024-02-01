from django.contrib import admin
from .models import (
    MedicalInformation,
    Diagnosis,
    Patient,
    PatientImage,
)


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
        "insurance",
    )
    search_fields = (
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "insurance",
    )
    list_filter = ("gender", "created_at", "updated_at")


@admin.register(PatientImage)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("patient", "image", "description", "uploaded_at")
    search_fields = ("patient__first_name", "patient__last_name", "description")
    list_filter = ("uploaded_at",)
