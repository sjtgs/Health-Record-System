from django.contrib import admin
from dashboard_app.models import PatientReview


@admin.register(PatientReview)
class PatientReviewAdmin(admin.ModelAdmin):
    list_display = ("doctor", "patient", "review_date", "purpose_review")
    search_fields = (
        "doctor__first_name",
        "doctor__last_name",
        "patient__first_name",
        "patient__last_name",
    )
    list_filter = ("review_date",)
