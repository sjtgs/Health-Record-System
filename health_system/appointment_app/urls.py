from django.urls import path
from appointment_app.views import  appointment_events , upload_and_extract_text, patient_medical_info

urlpatterns = [
    # path("schedule/<int:auto_id>/", schedule_appointment, name="schedule_appointment"),
    path("events/", appointment_events, name="appointment_events"),
    path("appointment_medical_notes/", upload_and_extract_text, name="appointment_medical_notes"),
    path("patient_info/", patient_medical_info, name="patient_info"),
]
