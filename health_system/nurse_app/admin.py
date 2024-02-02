# admin.py
from django.contrib import admin
from .models import Nurse, NurseImage, Appointment


@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
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
        "specialization",
    )
    search_fields = (
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "specialization",
    )
    list_filter = (
        "gender",
        "created_at",
        "updated_at",
        "specialization",
    )


@admin.register(NurseImage)
class NurseImageAdmin(admin.ModelAdmin):
    list_display = ("nurse", "image", "description", "uploaded_at")
    search_fields = ("nurse__first_name", "nurse__last_name", "description")
    list_filter = ("uploaded_at",)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("doctor", "patient", "appointment_date", "purpose")
    search_fields = (
        "doctor__first_name",
        "doctor__last_name",
        "patient__first_name",
        "patient__last_name",
    )
    list_filter = ("appointment_date",)
