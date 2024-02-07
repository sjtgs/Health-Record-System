# Doctor_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("patient-lists/", views.PatientsLists, name="patient-lists"),
    path("doctor-lists/", views.DoctorLists, name="doctor-lists"),
    path("nurse-lists/", views.NurseLists, name="nurse-lists"),
]
