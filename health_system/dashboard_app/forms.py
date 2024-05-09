from django import forms
from dashboard_app.models import AppointmentReview


class AppointmentReviewForm(forms.ModelForm):
    class Meta:
        model = AppointmentReview
        fields = ["doctor", "nurse", "patient", "appointment_date", "purpose"]
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
