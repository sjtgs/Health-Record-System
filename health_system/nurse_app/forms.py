from django import forms
from nurse_app.models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["doctor", "patient", "appointment_date", "purpose"]
        widgets = {
            "appointment_date": forms.DateInput(
                format=("%d-%m-%Y"),
                attrs={
                    "class": "form-control",
                    "placeholder": "Book Appointment date",
                    "type": "date",
                },
            ),
        }
