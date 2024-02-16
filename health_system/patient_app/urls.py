# patient_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from patient_app.views import (
    PatientLists,
    PatientViewSet,
    patient_login,
    patient_form,
    patient_form_edit,
)

patient_router = DefaultRouter()
patient_router.register(r"patients", PatientViewSet)

urlpatterns = [
    path("patients/", include(patient_router.urls)),
    path("login/", patient_login, name="patient_login"),
    path("patient-form/", patient_form, name="patient-form"),
    path("patient-lists/", PatientLists, name="patient-lists"),
    path(
        "<int:auto_id>/patient-form-edit/", patient_form_edit, name="patient-form-edit"
    ),
]
