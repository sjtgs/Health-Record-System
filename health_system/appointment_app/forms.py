from django import forms
from appointment_app.models import Appointment


# Created Appointment forms
class AppointmentForms(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["date", "time", "reason"]
