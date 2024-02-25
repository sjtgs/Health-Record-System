# Administration_app/urls.py
from django.urls import path
from administration_app.views import (
    view_all_records,
    doctor_lists,
    nurse_lists,
    patient_lists,
    doctor_specialization_chart,
    doctor_experience_chart,
)


urlpatterns = [
    path("admin-dashboard/", view_all_records, name="admin-dashboard"),
    path("doctor-lists/", doctor_lists, name="doctor-lists"),
    path("nurse-lists/", nurse_lists, name="nurse-lists"),
    path("patient-lists/", patient_lists, name="patient-lists"),
    path(
        "specialization-chart/",
        doctor_specialization_chart,
        name="specialization-chart",
    ),
    path("doctor-experience/", doctor_experience_chart, name="doctor-experience"),
]
