from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import Doctor, DoctorImage


def export_doctors(modelsadmin, request, queryset):
    response = HttpResponse(content="text/csv")
    response["Content-Disposition"] = 'attachment; filename="doctor_records.csv"'

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

    for doctor in queryset:
        writer.writerow(
            [
                doctor.auto_id,
                doctor.first_name,
                doctor.last_name,
                doctor.date_of_birth,
                doctor.gender,
                doctor.nrc,
                doctor.provinces,
                doctor.towns,
                doctor.address,
                doctor.email,
                doctor.phone_number,
                doctor.created_at,
                doctor.updated_at,
            ]
        )
    return response


export_doctors.short_description = "Export selected Doctors to CSV"


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        "auto_id",
        "user",
        "first_name",
        "last_name",
        "date_of_birth",
        "gender",
        "nrc",
        "countries",
        "provinces",
        "towns",
        "address",
        "medical_number",
        "hospitals",
        "specialization",
        "years_of_experience",
        "email",
        "phone_number",
        "created_at",
        "updated_at",
    )
    search_fields = ("first_name", "last_name", "nrc", "email", "phone_number")
    list_filter = (
        "gender",
        "countries",
        "provinces",
        "towns",
        "hospitals",
        "years_of_experience",
        "created_at",
        "updated_at",
    )
    actions = [export_doctors]


@admin.register(DoctorImage)
class DoctorImageAdmin(admin.ModelAdmin):
    list_display = ("doctor", "image", "description", "uploaded_at")
    search_fields = ("doctor__first_name", "doctor__last_name", "description")
    list_filter = ("uploaded_at",)
