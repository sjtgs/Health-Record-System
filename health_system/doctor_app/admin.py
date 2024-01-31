from django.contrib import admin
from .models import Doctor, DoctorImage


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        "auto_id",
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


@admin.register(DoctorImage)
class DoctorImageAdmin(admin.ModelAdmin):
    list_display = ("doctor", "image", "description", "uploaded_at")
    search_fields = ("doctor__first_name", "doctor__last_name", "description")
    list_filter = ("uploaded_at",)
