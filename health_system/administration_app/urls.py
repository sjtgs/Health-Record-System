# Administration_app/urls.py
from django.urls import path
from administration_app.views import (
    view_all_records,
    doctor_lists,
    nurse_lists,
    patient_lists,
    doctor_specialization_chart,
    doctor_experience_chart,
    administrator_form,
    administrator_form_edit,
    admin_administrator_detail,
    doctor_form,
    doctor_form_edit,
    admin_doctor_detail,
    nurse_form,
    nurse_form_edit,
    admin_nurse_detail,
    patient_form,
    patient_form_edit,
    admin_patient_detail,
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
    path("administration-form/", administrator_form, name="administration-form"),
    path(
        "<int:auto_id>/administrator-form-edit/",
        administrator_form_edit,
        name="administrator-form-edit",
    ),
    path(
        "administrator-detail/<int:auto_id>/",
        admin_administrator_detail,
        name="administrator-detail",
    ),
    path("doctor-form/", doctor_form, name="doctor-form"),
    path("<int:auto_id>/doctor-form-edit/", doctor_form_edit, name="doctor-form-edit"),
    path(
        "admin-doctor-detail/<int:auto_id>/",
        admin_doctor_detail,
        name="admin-doctor-detail",
    ),
    path("nurse-form/", nurse_form, name="nurse-form"),
    path("<int:auto_id>/nurse-form-edit/", nurse_form_edit, name="nurse-form-edit"),
    path(
        "admin-nurse-detail/<int:auto_id>/",
        admin_nurse_detail,
        name="admin-nurse-detail",
    ),
    path("patient-form/", patient_form, name="patient-form"),
    path(
        "<int:auto_id>/patient-form-edit/", patient_form_edit, name="patient-form-edit"
    ),
    path(
        "admin-patient-detail/<int:auto_id>/",
        admin_patient_detail,
        name="admin-patient-detail",
    ),
]
