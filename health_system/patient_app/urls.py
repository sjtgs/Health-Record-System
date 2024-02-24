# patient_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from patient_app.views import (
    PatientLists,
    PatientViewSet,
    patient_dashboard,
    patient_form,
    patient_form_edit,
    patient_detail,
)

patient_router = DefaultRouter()
patient_router.register(r"patients", PatientViewSet)

urlpatterns = [
    path("patients/", include(patient_router.urls)),
    path("patient-dashboard/", patient_dashboard, name="patient-dashboard"),
    path("patient-form/", patient_form, name="patient-form"),
    path("patient-lists/", PatientLists, name="patient-lists"),
    path(
        "<int:auto_id>/patient-form-edit/", patient_form_edit, name="patient-form-edit"
    ),
    path("patient-detail/<int:auto_id>/", patient_detail, name="patient-detail"),
]
