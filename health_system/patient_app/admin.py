from django.contrib import admin
from django.http import HttpResponse
import csv
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


def export_patients(modeladmin, request, queryset):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="patient_records.csv"'

    writer = csv.writer(response)
    writer.writerow(
        [
            "ID",
            "First Name",
            "Last Name",
            "Date of Birth",
            "Gender",
            "NRC",
            "Province",
            "Town",
            "Address",
            "Email",
            "Phone Number",
            "Created At",
            "Updated At",
        ]
    )

    for patient in queryset:
        writer.writerow(
            [
                patient.auto_id,
                patient.first_name,
                patient.last_name,
                patient.date_of_birth,
                patient.gender,
                patient.nrc,
                patient.provinces,
                patient.towns,
                patient.address,
                patient.email,
                patient.phone_number,
                patient.created_at,
                patient.updated_at,
            ]
        )

    return response


export_patients.short_description = "Export selected patients to CSV"


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "auto_id",
        "first_name",
        "last_name",
        "date_of_birth",
        "gender",
        "patient_type",
        "blood_type",
        "patient_unit",
        "email",
        "phone_number",
        "created_at",
        "updated_at",
        "insurance",
    )
    search_fields = (
        "user",
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "insurance",
    )
    list_filter = ("user", "gender", "created_at", "updated_at")
    actions = [export_patients]


@admin.register(PatientImage)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("patient", "image", "description", "uploaded_at")
    search_fields = ("patient__first_name", "patient__last_name", "description")
    list_filter = ("uploaded_at",)
