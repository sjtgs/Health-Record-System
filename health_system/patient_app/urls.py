# patient_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import view_patient_records, PatientLists, PatientViewSet

patient_router = DefaultRouter()
patient_router.register(r"patients", PatientViewSet)

urlpatterns = [
    path("patients/", include(patient_router.urls)),
    path("patient-records/", view_patient_records, name="view_patient_records"),
    path("patient-lists/", PatientLists, name="patient-lists"),
    # Add other patient-related URLs
]
