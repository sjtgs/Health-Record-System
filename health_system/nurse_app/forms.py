from django import forms
from nurse_app.models import Appointment


class AppointmentForm(forms.ModefForm):
    class Meta:
        model = Appointment
        fields = ["doctor", "patient", "appointment_date", "purpose"]
