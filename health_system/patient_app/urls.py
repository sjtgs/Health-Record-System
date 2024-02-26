# patient_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from patient_app.views import (
    PatientViewSet,
    view_patient_records,
    patient_detail,
)

patient_router = DefaultRouter()
patient_router.register(r"patients", PatientViewSet)

urlpatterns = [
    path("patients/", include(patient_router.urls)),
    path("patient-records/", view_patient_records, name="patient-dashboard"),
    path("patient-detail/<int:auto_id>/", patient_detail, name="patient-detail"),
]
