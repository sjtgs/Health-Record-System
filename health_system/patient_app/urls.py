# patient_app/urls.py
from django.urls import path
from .views import view_patient_records

urlpatterns = [
    path("patient-records/", view_patient_records, name="view_patient_records"),
    # Add other patient-related URLs
]
