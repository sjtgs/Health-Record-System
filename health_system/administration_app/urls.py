# Administration_app/urls.py
from django.urls import path
from administration_app.views import (
    view_all_records,
    doctor_lists,
    nurse_lists,
    patient_lists,
    # view_pie_chart,
)


urlpatterns = [
    path("admin-dashboard/", view_all_records, name="admin-dashboard"),
    path("doctor-lists/", doctor_lists, name="doctor-lists"),
    path("nurse-lists/", nurse_lists, name="nurse-lists"),
    path("patient-lists/", patient_lists, name="patient-lists"),
    # path("pie-chart/", view_pie_chart, name="pie-chart"),
]
