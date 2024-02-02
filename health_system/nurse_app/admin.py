# admin.py
from django.contrib import admin
from .models import Nurse, NurseImage


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
