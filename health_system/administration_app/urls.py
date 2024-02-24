# Administration_app/urls.py
from django.urls import path, include
from administration_app.views import doctor_lists, nurse_lists, patient_lists


urlpatterns = [
    path("doctor-lists/", doctor_lists, name="doctor-lists"),
    path("nurse-lists/", nurse_lists, name="nurse-lists"),
    path("patient-lists/", patient_lists, name="patient-lists"),
]
