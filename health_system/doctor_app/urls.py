# Doctor_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from doctor_app.views import (
    DoctorViewSet,
    PatientsLists,
    NurseLists,
    doctor_dashboard,
    view_doctor_record,
    doctor_detail,
    patient_detail,
    nurse_detail,
)

doctor_router = DefaultRouter()
doctor_router.register(r"doctors", DoctorViewSet)


urlpatterns = [
    path("doctors/", include(doctor_router.urls)),
    path("doctor-dashboard/", doctor_dashboard, name="doctor-dashboard"),
    path("doctor-record/", view_doctor_record, name="doctor-record"),
    path("patient-lists/", PatientsLists, name="patient-lists"),
    path("nurse-lists/", NurseLists, name="nurse-lists"),
    path("doctor-detail/<int:auto_id>/", doctor_detail, name="doctor-detail"),
    path("patient-detail/<int:auto_id>/", patient_detail, name="patient-detail"),
    path("nurse-detail/<int:auto_id>/", nurse_detail, name="nurse-detail"),
]
