# Doctor_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from doctor_app.views import (
    DoctorViewSet,
    PatientsLists,
    DoctorLists,
    NurseLists,
    doctor_login,
    doctor_form,
)

doctor_router = DefaultRouter()
doctor_router.register(r"doctors", DoctorViewSet)

#
urlpatterns = [
    path("doctors/", include(doctor_router.urls)),
    path("login/", doctor_login, name="doctor_login"),
    path("patient-lists/", PatientsLists, name="patient-lists"),
    path("doctor-lists/", DoctorLists, name="doctor-lists"),
    path("nurse-lists/", NurseLists, name="nurse-lists"),
    path("doctor-form/", doctor_form, name="doctor-form"),
]
