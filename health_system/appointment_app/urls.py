from django.urls import path
from appointment_app.views import schedule_appointment, appointment_events

urlpatterns = [
    path("schedule/<int:auto_id>/", schedule_appointment, name="schedule_appointment"),
    path("events/", appointment_events, name="appointment_events"),
]
