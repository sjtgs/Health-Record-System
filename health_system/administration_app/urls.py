# Administration_app/urls.py
from django.urls import path
from administration_app.views import (
    view_all_records,
    doctor_lists,
    nurse_lists,
    patient_lists,
    doctor_specialization_chart,
    doctor_experience_chart,
    doctor_form,
    doctor_form_edit,
    nurse_form,
    nurse_form_edit,
    patient_form,
    patient_form_edit,
)


urlpatterns = [
    path("admin-dashboard/", view_all_records, name="admin-dashboard"),
    path(
        "specialization-chart/",
        doctor_specialization_chart,
        name="specialization-chart",
    ),
    path("doctor-lists/", doctor_lists, name="doctor-lists"),
    path("nurse-lists/", nurse_lists, name="nurse-lists"),
    path("patient-lists/", patient_lists, name="patient-lists"),
    path("doctor-experience/", doctor_experience_chart, name="doctor-experience"),
    path("doctor-form/", doctor_form, name="doctor-form"),
    path("<int:auto_id>/doctor-form-edit/", doctor_form_edit, name="doctor-form-edit"),
    path("nurse-form/", nurse_form, name="nurse-form"),
    path("<int:auto_id>/nurse-form-edit/", nurse_form_edit, name="nurse-form-edit"),
    path("patient-form/", patient_form, name="patient-form"),
    path(
        "<int:auto_id>/patient-form-edit/", patient_form_edit, name="patient-form-edit"
    ),
]
