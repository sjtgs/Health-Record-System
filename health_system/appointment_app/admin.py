from django.contrib import admin
from appointment_app.models import Appointment


# Register your models here.
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "patient",
        "doctor",
        "date",
        "time",
        "reason",
    )
    search_fields = (
        "patient",
        "date",
        "time," "reason",
    )
    list_filter = ("created_at",)
